from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.4, api_key=openai_api_key)

# 📜 Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful and knowledgeable smart city utility assistant. You can answer questions about electricity, water, and waste management."),
    ("human", "{query}")
])

# 🔗 Chain Assembly
utility_chain = prompt | llm | StrOutputParser()

# 🚀 Entry Function
def run_utility_agent(query: str) -> str:
    return utility_chain.invoke({"query": query})


'''
if __name__ == "__main__":
    while True:
        query = input("Ask the Utility Agent (type 'exit' to quit):\n> ")
        if query.lower() == "exit":
            break
        print(run_utility_agent(query))
'''