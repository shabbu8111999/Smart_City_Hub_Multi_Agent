from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableMap
from dotenv import load_dotenv
import os


load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.3,
    api_key=openai_api_key
)


prompt = ChatPromptTemplate.from_template("""
You are a helpful health assistant for a smart city.

Respond with concise, factual health-related answers.
If the query is not health-related, reply: "I'm a health assistant and cannot help with that."

User Query: {query}
""")


def post_process(response):
    return response.content.strip()

# Chain using RunnableMap + LLM + RunnableLambda
chain = (
    RunnableMap({"query": lambda x: x["query"]}) |  # prepares input
    prompt |
    llm |
    RunnableLambda(post_process)
)

# Function for external use
def run_health_agent(query: str) -> str:
    return chain.invoke({"query": query})


"""
# Quick test
if __name__ == "__main__":
    test_query = "What to do in case of a heat stroke?"  #"What to do when car engine goes down?"
    print("Health Agent Response:")
    print(run_health_agent(test_query))
"""