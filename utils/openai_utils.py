import os
from langchain_openai import ChatOpenAI

def init_openai(api_key: str) -> ChatOpenAI:
    if not api_key:
        raise ValueError("OpenAI API key is required")
    os.environ["OPENAI_API_KEY"] = api_key
    return ChatOpenAI(temperature=0)
