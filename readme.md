# Multi-Agent Research Assistant

## Overview
A system leveraging LangChain and LangGraph to process and refine academic PDFs through three key stages:
1. **Summarization**: Extracts key points from research content.
2. **Critique**: Analyzes summaries against related research for gaps and insights.
3. **Refinement**: Enhances summaries based on critique feedback.

---

## Setup

### Requirements
- **Python Version**: 3.8+
- **Packages**:
  - `langchain`
  - `langgraph`
  - `PyPDF2`
  - `requests`
  - `python-dotenv`
  - `faiss-cpu`

### Installation
```bash
pip install langchain langgraph PyPDF2 requests python-dotenv faiss-cpu
```

---
### Project Structure
```plaintext
project/
├── agents/
│   ├── summary_agent.py
│   ├── critique_agent.py
│   └── refinement_agent.py
├── utils/
│   ├── pdf_utils.py
│   └── openai_utils.py
|   └── vector_store.py
├── orchestration/
│   └── workflow.py
└── main.py
```
---

## Code Components

1. **`AgentState`**: Tracks the paper's processing state (raw text, summary, critique, refined output, and errors).
2. **`extract_text_from_pdf`**: Extracts text from a PDF file.
3. **`init_openai`**: Initializes the OpenAI language model.
4. **`create_summary_agent`**: Generates research summaries from text.
5. **`create_critique_agent`**: Critiques summaries by comparing them with related research.
6. **`create_refinement_agent`**: Refines summaries based on critiques.
7. **`create_vector_store`**: Creates a FAISS index for semantic search from text data.
8. **`create_research_workflow`**: Orchestrates the workflow using LangGraph.
9. **`process_pdf`**: Handles the full lifecycle of PDF processing (summarization, critique, refinement).
10. **`main`**: Entry point to execute the script.

---

## Running

### Environment Setup
Create a `.env` file:
```dotenv
OPENAI_API_KEY=your_api_key_here
PDF_PATH=/path/to/your/pdf.pdf
```

### Execute Script
```bash
python main.py
```

---

## Workflow
```plaintext
Summarize -> Critique -> Refine
```

1. **Summarize**: Extracts key points from the PDF.
2. **Critique**: Fetches related research and critiques the summary.
3. **Refine**: Refines the summary using critique feedback.

---

## Example Output

### Summary
This research article presents a computer vision system for counting Twospot astyanax (*Astyanax bimaculatus*) oocytes in Petri dishes using images captured by smartphones. The proposed procedure involves image segmentation using the simple linear iterative clustering (SLIC) method and classification of superpixels into different categories using machine learning algorithms. Five machine learning algorithms were tested, with support vector machines (SVM) achieving the best result with 97% correct oocyte recognition. The study demonstrates the feasibility of using smartphones for oocyte counting in fish reproduction processes.

#### Key Points:
1. Proposed a computer vision system for oocyte counting using smartphone-captured images.
2. Utilized SLIC for image segmentation and machine learning algorithms for classification.
3. SVM achieved the highest accuracy of 97% in oocyte recognition.
4. Demonstrated the potential of smartphone-based image processing in aquaculture research.

#### Methods:
- Image segmentation using SLIC method.
- Classification of superpixels into oocyte, dirtiness, dark background, and light background.
- Feature extraction including color, gradient, texture, and shape characteristics.
- Evaluation of performance using metrics like CCR, precision, recall, F-measure, and ROC area.

#### Conclusions:
- The study successfully counted oocytes with 97% accuracy using SVM.
- Smartphone-based image processing can enhance efficiency in fish reproduction research.
- Future work includes applying deep learning methods and experimenting with other fish species.

---

### Critique
The research article presents a novel computer vision system for counting Twospot astyanax oocytes using smartphone-captured images, showcasing the potential of smartphone-based image processing in fish reproduction research. The study utilized the SLIC method for image segmentation and machine learning algorithms for classification, with SVM achieving the highest accuracy.

#### Gaps and Suggestions for Future Research:
1. The study mentions future work involving deep learning methods and experimentation with other fish species. Providing a roadmap for how these advancements could enhance the current system and expand its applicability would be valuable.
2. Investigating the scalability of the proposed system for large-scale oocyte counting in aquaculture settings could be a promising direction for future research.
3. Exploring the integration of real-time monitoring capabilities and automation features into the smartphone-based system could further improve its practical utility in fish reproduction processes.

#### In conclusion:
While the research article presents an innovative approach to oocyte counting using smartphone-based image processing, there are opportunities to enhance the completeness of the study by addressing the suggested improvements and gaps for future research.

---

### Final Output
The research article introduces a computer vision system for counting Twospot astyanax oocytes in Petri dishes using smartphone-captured images. The system employs the SLIC method for image segmentation and machine learning algorithms for classification, with support vector machines (SVM) achieving 97% accuracy in oocyte recognition. The study highlights the potential of smartphone-based image processing in fish reproduction research, showcasing the efficiency and feasibility of this approach. 

#### Future Directions:
- Exploring deep learning methods.
- Testing with other fish species.
- Assessing scalability for large-scale applications.
- Integrating real-time monitoring and automation features.

Addressing the critique feedback, the study could enhance its abstract, provide more detailed discussions on limitations and comparisons with existing methods, and offer a roadmap for future advancements to improve system applicability and effectiveness. By incorporating these suggestions, the research can further solidify its contribution to the field of aquaculture research.



