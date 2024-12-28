import requests
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from typing import Callable, Dict


def create_critique_agent(llm: ChatOpenAI) -> Callable[[Dict], Dict]:
    critique_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a research critic analyzing for completeness, accuracy, and comparing with existing research. Identify gaps and suggest improvements."),
        ("user", "Review and critique:\nSummary: {summary}\nRelated Papers: {related_papers}")
    ])

    def fetch_related_papers(query: str):
        try:
            response = requests.get("https://api.crossref.org/works", params={"query": query, "rows": 5})
            if response.status_code == 200:
                data = response.json()
                papers = [
                    {
                        "title": item["title"][0] if "title" in item and item["title"] else "No title available",
                        "abstract": item["abstract"] if "abstract" in item else "No abstract available"
                    }
                    for item in data["message"]["items"]
                ]
                return papers
            print(f"CrossRef API error: {response.status_code}")
            return []
        except Exception as e:
            print(f"Paper fetch error: {str(e)}")
            return []

    def critique(state: Dict) -> Dict:
        print("Starting critique...")

        try:
            related_papers = fetch_related_papers(state["summary"][:200])
            papers_text = "\n".join([f"Title: {p['title']}\nAbstract: {p['abstract']}" for p in related_papers])
            
            chain = critique_prompt | llm
            critique = chain.invoke({
                "summary": state["summary"],
                "related_papers": papers_text
            })
            if hasattr(critique, 'content'):
                state["critique"] = critique.content
            else:
                print(f"Unexpected response structure from LLM: {critique}")
                state["error"] = "Unexpected response structure from LLM"
            print("Critique complete")
        except Exception as e:
            print(f"Critique error: {str(e)}")
            state["error"] = f"Critique error: {str(e)}"
        return state

    return critique