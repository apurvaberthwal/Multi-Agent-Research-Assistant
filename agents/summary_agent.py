from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from typing import Callable, Dict
import logging

def create_summary_agent(llm: ChatOpenAI) -> Callable[[Dict], Dict]:
    summary_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a research summarization expert. Extract key points, methods, and conclusions."),
        ("user", "Summarize the following research content:\n\n{text}")
    ])

    def summarize(state: Dict) -> Dict:
        try:
            print("Starting summarization...")
            chain = summary_prompt | llm
            summary = chain.invoke({"text": state["original_text"]})
            if hasattr(summary, 'content'):
                state["summary"] = summary.content
                print("Summarization complete")
            else:
                print(f"Unexpected response structure from LLM: {summary}")
                state["error"] = "Unexpected response structure from LLM"
        except Exception as e:
            print(f"Summarization error: {str(e)}")
            state["error"] = f"Summarization error: {str(e)}"
        return state
    
    return summarize
