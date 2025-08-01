from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.3,
    api_key=openai_api_key
)

# Prompt for Pollution Monitoring Agent
prompt = ChatPromptTemplate.from_template(
    """
    You are a Pollution Monitoring Agent in a Smart City AI system.

    Your responsibility is to assess the air quality and suggest suitable actions if pollution levels are high.
    
    Respond briefly and clearly. Do not include unnecessary details.

    Example:
    Input: "Pollution level in sector 9 is AQI 180"
    Output:
    1. Issue a health advisory to residents in sector 9.
    2. Restrict construction and outdoor burning activities.
    3. Increase frequency of air quality monitoring.

    Input: {query}
    """
)


chain = prompt | llm


def run_pollution_agent(query: str) -> str:
    result = chain.invoke({"query": query})
    return str(result.content if hasattr(result, "content") else result)


'''
# Test
if __name__ == "__main__":
    test_query = "Pollution level in sector 7 is AQI 250"
    print("Pollution Agent Response:")
    print(run_pollution_agent(test_query))
'''