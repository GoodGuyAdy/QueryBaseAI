from Constant.LLM import LLMProvider
from QueryBaseAI.settings import CURRENT_LLM_PROVIDER
from LLM.Response.Provider.Providers import AIResponseProvider
from Core.Search.ContextSearch import semantic_search, keyword_search


def get_ai_response(query, org, file_id=None):
    """
    Generates AI response based on current LLM provider
    """

    ai_response = AIResponseProvider()

    vector_search_context = semantic_search(query, org, file_id)
    keyword_search_context = keyword_search(query, org, file_id)

    context = f"""
    Vector Search Context: {vector_search_context}.
    Keyword Search Context: {keyword_search_context}
    """

    if CURRENT_LLM_PROVIDER == LLMProvider.ai21:
        response = ai_response.generate_ai21_response(query, context)

    elif CURRENT_LLM_PROVIDER == LLMProvider.open_ai:
        response = ai_response.generate_openai_response(query, context)

    return response
