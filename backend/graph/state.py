from typing import Annotated, Optional

from typing_extensions import TypedDict

from langgraph.graph.message import add_messages


class FatLossAgentState(TypedDict):

    messages: Annotated[list, add_messages]

    user_query: str

    agent_name: Optional[str]

    tool_name: Optional[str]

    tool_output: Optional[dict]

    meal_history: list

    workout_history: list

    body_metrics: dict

    daily_totals: dict

    final_response: Optional[dict]