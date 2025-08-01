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


prompt = ChatPromptTemplate.from_template(
    """
    You are a planning assistant in a Smart City multi-agent system.

    Your task is to create a clear, actionable plan based on the user's request.
    Each plan should include logical, step-by-step actions to address the issue described.

    Follow these instructions strictly:
    - Respond only with the list of steps, using numbered bullets.
    - Be brief but specific in each step.
    - Focus only on the task described — no general information.

    Example:

    Input:
    "There's a water shortage in sector 5"

    Output:
    1. Alert the utility department about the shortage in sector 5.
    2. Schedule and dispatch water tankers to sector 5.
    3. Notify residents in sector 5 via SMS and city alert systems.

    Now create a plan for the following request:

    {query}
    """
)


# 3. Chain Prompt + LLM
chain = prompt | llm


def run_planner_agent(query: str) -> str:
    result = chain.invoke({"query": query})
    return str(result.content if hasattr(result, "content") else result)



planner_runnable = RunnableLambda(run_planner_agent)


'''
# Test
if __name__ == "__main__":
    test_query = "There's a power outage in zone B"
    print("Planner Agent Response:")
    print(run_planner_agent(test_query))
'''