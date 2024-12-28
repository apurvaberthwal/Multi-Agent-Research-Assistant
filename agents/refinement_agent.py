from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from typing import Callable, Dict
import logging
def create_refinement_agent(llm: ChatOpenAI) -> Callable[[Dict], Dict]:
    refinement_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a content refinement expert. Your task is to combine the critique feedback with the original summary to produce a refined, cohesive output. Ensure clarity, logical flow, and concise language in the final summary. Add citations or references for supporting information where appropriate."),
        ("user", "Refine this content using the critique:\nSummary: {summary}\nCritique: {critique}")
    ])

    
    def refine(state: Dict) -> Dict:
        logging.info("Starting refinement...")
        try:
            print("Starting refinement...")
            chain = refinement_prompt | llm
            refined = chain.invoke({
                "summary": state["summary"],
                "critique": state["critique"]
            })
            if hasattr(refined, 'content'):
                state["final_output"] = refined.content
             
            else:
                print(f"Unexpected response structure from LLM: {refined}")
                state["error"] = "Unexpected response structure from LLM"
            print("Refinement complete")
        except Exception as e:
            print(f"Refinement error: {str(e)}")
            state["error"] = f"Refinement error: {str(e)}"
        return state
    return refine