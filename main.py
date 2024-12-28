from utils.pdf_utils import extract_text_from_pdf
from orchestration.workflow import create_research_workflow
from dotenv import load_dotenv
import os

def main():
    
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    pdf_path = os.getenv("PDF_PATH")

    if not (api_key and pdf_path and os.path.exists(pdf_path)):
        print("Missing configuration or file path.")
        return

    workflow = create_research_workflow(api_key)
    paper_text = extract_text_from_pdf(pdf_path)

    initial_state = {
        "original_text": paper_text,
        "summary": "",
        "critique": "",
        "final_output": "",
        "error": ""
    }
    print("Starting academic content processing...\n")
    result = workflow.invoke(initial_state)
    print("Workflow execution completed successfully.\n")
    print("Final output: \n")
    if "error" in result and result["error"]:
        print(f"Error: {result['error']}")
    else:
        
        print(f"Summary: {result['summary']}")
        print("\n")
        print(f"Critique: {result['critique']}")
        print("\n")
        print(f"Refined Output: {result['final_output']}")
        print("\n")
        
if __name__ == "__main__":
    main()
