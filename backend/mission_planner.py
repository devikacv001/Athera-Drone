from typing import TypedDict
from langgraph.graph import StateGraph, END

class MissionState(TypedDict):
    items: dict
    plan: list

def create_plan(state):

    items = state["items"]

    plan = [
        "Find nearby shops",
        "Collect available items",
        "Move to next shop if needed",
        "Return when complete"
    ]

    return {
        "items": items,
        "plan": plan
    }

builder = StateGraph(MissionState)

builder.add_node(
    "mission_planner",
    create_plan
)

builder.set_entry_point(
    "mission_planner"
)

builder.add_edge(
    "mission_planner",
    END
)

graph = builder.compile()