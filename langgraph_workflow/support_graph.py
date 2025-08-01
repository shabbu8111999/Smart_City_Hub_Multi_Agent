from langchain_core.runnables import RunnableLambda
from langgraph.graph import StateGraph
from smartCity.agents.classifier_agent import classifier_runnable
from smartCity.agents.health_agent import run_health_agent
from smartCity.agents.traffic_agent import handle_traffic_query
from smartCity.agents.pollution_agent import run_pollution_agent
from smartCity.agents.utility_agent import run_utility_agent
from smartCity.agents.planner_agent import planner_runnable
from smartCity.agents.executor_agent import executor_runnable
from typing import Optional
from pydantic import BaseModel


# Wrap legacy functions as Runnables, access .input attribute of AgentState
def wrap_agent(agent_func):
    return RunnableLambda(lambda inputs: {"output": agent_func(inputs.input)})


health_runnable = wrap_agent(run_health_agent)
traffic_runnable = wrap_agent(handle_traffic_query)
pollution_runnable = wrap_agent(run_pollution_agent)
utility_runnable = wrap_agent(run_utility_agent)


# Router logic returns a dict with "domain" key
def router(inputs):
    query = inputs.input.lower()
    if any(word in query for word in ["health", "doctor", "fever", "pain", "stroke"]):
        return {"output": "health"}
    elif any(word in query for word in ["traffic", "road", "accident", "congestion"]):
        return {"output": "traffic"}
    elif any(word in query for word in ["pollution", "smog", "air quality", "aqi"]):
        return {"output": "pollution"}
    elif any(word in query for word in ["water", "electricity", "power", "waste"]):
        return {"output": "utility"}
    else:
        return {"output": "unknown"}



router_runnable = RunnableLambda(router)


class AgentState(BaseModel):
    input: str
    classification: Optional[str] = None
    domain: Optional[str] = None
    plan: Optional[str] = None
    final_response: Optional[str] = None


workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("classifier", classifier_runnable)
workflow.add_node("router", router_runnable)
workflow.add_node("health_agent", health_runnable)
workflow.add_node("traffic_agent", traffic_runnable)
workflow.add_node("pollution_agent", pollution_runnable)
workflow.add_node("utility_agent", utility_runnable)

workflow.add_node("planner_agent", planner_runnable)
workflow.add_node("executor_agent", executor_runnable)

# Edges: classifier -> router
workflow.add_edge("classifier", "router")

# Router conditional edges to domain-specific agents
workflow.add_conditional_edges(
    "router",
    {
        "health": RunnableLambda(lambda _: "health_agent"),
        "traffic": RunnableLambda(lambda _: "traffic_agent"),
        "pollution": RunnableLambda(lambda _: "pollution_agent"),
        "utility": RunnableLambda(lambda _: "utility_agent"),
        "unknown": RunnableLambda(lambda _: "executor_agent"),
    }
)

# Domain-specific agents -> planner
workflow.add_edge("health_agent", "planner_agent")
workflow.add_edge("traffic_agent", "planner_agent")
workflow.add_edge("pollution_agent", "planner_agent")
workflow.add_edge("utility_agent", "planner_agent")

# Planner -> executor
workflow.add_edge("planner_agent", "executor_agent")

# Set entry and finish points
workflow.set_entry_point("classifier")
workflow.set_finish_point("executor_agent")

# Compile the graph
app = workflow.compile()


def run_support_graph(query: str):
    result = app.invoke({"input": query})
    return result


if __name__ == "__main__":
    queries = [
        "There is heavy traffic near downtown due to accident.",
        "Power outage reported in Sector 9.",
        "High AQI levels in the industrial area.",
        "Need ambulance for a stroke victim.",
    ]

    for i, query in enumerate(queries, 1):
        print(f"\n🟠 Query {i}: {query}")
        result = run_support_graph(query)
        print("✅ Output:")
        print(result)
