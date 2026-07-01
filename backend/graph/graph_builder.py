from langgraph.graph import StateGraph, START, END

from backend.graph.state import FatLossAgentState

from backend.graph.nodes import (
    supervisor_node,
    nutrition_node,
    fitness_node,
    body_node,
    coach_node
)

from backend.graph.router import route_agent

builder = StateGraph(FatLossAgentState)

builder.add_node("supervisor", supervisor_node)

builder.add_node("nutrition", nutrition_node)

builder.add_node("fitness", fitness_node)

builder.add_node("body", body_node)

builder.add_node("coach", coach_node)

builder.add_edge(START, "supervisor")

builder.add_conditional_edges(

    "supervisor",

    route_agent,

    {

        "nutrition": "nutrition",

        "fitness": "fitness",

        "body": "body",

        "coach": "coach"

    }

)

builder.add_edge("nutrition", END)

builder.add_edge("fitness", END)

builder.add_edge("body", END)

builder.add_edge("coach", END)

graph = builder.compile()