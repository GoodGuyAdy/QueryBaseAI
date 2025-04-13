import os
from ai21 import AI21Client
from Constant.LLM import LLMProvider
from langchain_openai import ChatOpenAI
from QueryBaseAI.settings import CURRENT_LLM_PROVIDER


def llm_client():
    """
    Initializes LLM client object based on current LLM provider
    """
    if CURRENT_LLM_PROVIDER == LLMProvider.ai21:
        client = AI21Client(api_key=os.environ.get("AI21_API_KEY"))

    if CURRENT_LLM_PROVIDER == LLMProvider.open_ai:
        client = ChatOpenAI(
            api_key=os.environ.get("AI21_API_KEY"),
            model="gpt-3.5-turbo",
            max_tokens=1024,
            temperature=0.4,
        )

    return client
