from fastapi import APIRouter
from backend.graph.graph_builder import graph
from backend.schemas.request_schema import ChatRequest

from backend.schemas.response_schema import ChatResponse

from backend.services.session_manager import SessionManager

router = APIRouter()
session = SessionManager()

@router.get("/")

def home():
    return {
        "message" : "Fat loss agent api running"
    }

@router.get("/health")

def health():

    return {

        "status": "healthy"

    }

@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    session.set_query(

        request.message

    )

    result = graph.invoke(

        session.get_state()

    )

    session.update_state(

        result

    )

    state = session.get_state()

    return ChatResponse(

        agent=result["agent_name"],

        response=result["final_response"],

        summary={

            "calories":

                state["daily_totals"]["calories"],

            "protein":

                state["daily_totals"]["protein"],

            "burned":

                round(

                    sum(

                        w.get(

                            "calories_burned",

                            0

                        )

                        for w in state["workout_history"]

                    ),

                    2

                )

        }

    )

@router.post("/reset")

def reset():
    session.reset()

    return {
        "message" : "Session Reset Successfully"
    }