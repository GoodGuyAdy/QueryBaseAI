from LLM.Client.Main import llm_client
from ai21.models.chat import ChatMessage, ResponseFormat


class AIResponseProvider:
    """
    Every LLM has different way of calling them. Define it here.
    """

    def __init__(self):
        """
        Assign LLM client
        """
        self.client = llm_client()

    def generate_openai_response(self, query, context):
        """
        Generates response from query and context from OpenAI
        """

        prompt = f"""
        Human: I need information on the following query:
        {query}
        
        Here is relevant context to help answer the query:
        {context}
        
        Please answer based on the context provided. If the context doesn't contain relevant information to answer the query, please indicate that.
        
        Assistant:
        """

        response = self.client.generate([prompt])
        return response.generations[0][0].text

    def generate_ai21_response(self, query, context):
        """
        Generates response from query and context from AI21
        """

        messages = [
            ChatMessage(
                role="user",
                content=f"I need information on the following query: {query}",
            ),
            ChatMessage(
                role="user",
                content=f"Here is relevant context to help answer the query:\n{context}",
            ),
            ChatMessage(
                role="assistant",
                content="Please answer based on the context provided. If the context doesn't contain relevant information, indicate that.",
            ),
        ]

        response = self.client.chat.completions.create(
            model="jamba-large-1.6",
            messages=messages,
            max_tokens=1024,
            temperature=0.4,
            n=1,
            response_format=ResponseFormat(type="text"),
        )

        answer = response.choices[0].message.content
        return answer
