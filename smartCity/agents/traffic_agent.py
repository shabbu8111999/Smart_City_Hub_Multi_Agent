from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")


llm = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo", temperature=0.3)


prompt = ChatPromptTemplate.from_template(
    """
    You are a traffic assistance agent for a smart city.
    Provide helpful and concise answers to traffic-related queries.

    Query: {query}
    Response:    
    """
)


traffic_chain = prompt | llm


def handle_traffic_query(query: str) -> str:
    """ Processes a traffic related query """
    response = traffic_chain.invoke({"query" : query})
    return response.content.strip()


'''
if __name__ == "__main__":
    test_query = "Is there any traffic congestion near the city center?"
    reply = handle_traffic_query(test_query)
    print(f"Response: {reply}")
    '''