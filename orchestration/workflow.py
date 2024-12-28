from langgraph.graph import Graph
from agents.summary_agent import create_summary_agent
from agents.critique_agent import create_critique_agent
from agents.refinement_agent import create_refinement_agent
from utils.openai_utils import init_openai

def create_research_workflow(api_key: str):
    llm = init_openai(api_key)

    summarize = create_summary_agent(llm)
    critique = create_critique_agent(llm)
    refine = create_refinement_agent(llm)

    workflow = Graph()
    workflow.add_node("summarize", summarize)
    workflow.add_node("critique", critique)
    workflow.add_node("refine", refine)
    workflow.add_edge("summarize", "critique")
    workflow.add_edge("critique", "refine")
    workflow.set_entry_point("summarize")
    workflow.set_finish_point("refine")

    return workflow.compile()
