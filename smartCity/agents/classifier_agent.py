from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableMap
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.2,
    api_key=openai_api_key
)


prompt = ChatPromptTemplate.from_template("""
You are a smart classifier agent in a Smart City Hub.

Given a user query, classify it into one of these categories:
- "health"
- "traffic"
- "pollution"
- "utilities"
- "unknown" (if it doesn't fit any category)

Only respond with the category name (all lowercase, no explanation).
Query: {query}
""")

# Chain: prompt -> llm
chain = prompt | llm


def classify_query(query: str) -> str:
    response = chain.invoke({"query": query})
    return response.content.strip().lower()

# Runnable version (if needed in LangGraph)
classifier_runnable = RunnableLambda(lambda input: {"category": classify_query(input["query"])})

# Just a test
if __name__ == "__main__":
    test_query = "There's heavy traffic on Main Street. Any updates?"
    print("Detected category:", classify_query(test_query))

    