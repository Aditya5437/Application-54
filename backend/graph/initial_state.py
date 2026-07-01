from backend.graph.state import FatLossAgentState


def create_initial_state(user_query: str) -> FatLossAgentState:

    return {

        "messages": [],

        "user_query": user_query,

        "agent_name": None,

        "tool_name": None,

        "tool_output": None,

        "meal_history": [],

        "workout_history": [],

        "body_metrics": {},

        "daily_totals": {

            "calories": 0,

            "protein": 0,

            "carbs": 0,

            "fat": 0

        },

        "final_response": None

    }