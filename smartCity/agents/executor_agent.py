from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# LLM setup
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.3,
    api_key=openai_api_key
)

# Prompt Template for Executor
prompt = ChatPromptTemplate.from_template(
    """
    You are a task executor agent in a Smart City AI system.

    Your job is to simulate the execution of a single step from a plan.
    
    - Take the input step and generate a short confirmation of what action would be taken.
    - Do not repeat the input.
    - Keep the output short and formal.

    Example:

    Input Step:
    "Notify the utility department about the power outage in zone B."

    Output:
    "The utility department has been notified about the power outage in zone B."

    Now execute this step:

    Step: {step}
    """
)

# Chain: Prompt → LLM
chain = prompt | llm

# Executor Function
def run_executor_agent(step: str) -> str:
    result = chain.invoke({"step": step})
    return str(result.content if hasattr(result, "content") else result)

# Runnable for future chaining
executor_runnable = RunnableLambda(run_executor_agent)


'''
# Test Run
if __name__ == "__main__":
    test_step = "Notify the utility department about the power outage in zone B."
    print("Executor Agent Response:")
    print(run_executor_agent(test_step))
'''