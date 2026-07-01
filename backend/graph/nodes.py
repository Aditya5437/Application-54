from backend.agents.supervisor.supervisor_agent import SupervisorAgent
from backend.agents.nutrition.nutrition_agent import NutritionAgent
from backend.agents.fitness.fitness_agent import FitnessAgent
from backend.agents.body.body_agent import BodyAgent
from backend.agents.memory.memory_agent import MemoryAgent
from backend.agents.coach.coach_agent import CoachAgent

supervisor = SupervisorAgent()

nutrition_agent = NutritionAgent()

fitness_agent = FitnessAgent()

body_agent = BodyAgent()

memory_agent = MemoryAgent()

coach_agent = CoachAgent()


def supervisor_node(state):

    selected_agent = supervisor.route(

        state["user_query"]

    )

    return {

        "agent_name": selected_agent

    }


def nutrition_node(state):

    report = nutrition_agent.process_meal(

        state["user_query"]

    )

    updated = memory_agent.store_meal(

        state,

        report

    )

    return {

        **updated,

        "tool_output": report,

        "final_response": report

    }


def fitness_node(state):

    report = fitness_agent.process_workout(

        state["user_query"]

    )

    updated = memory_agent.store_workout(

        state,

        report

    )

    return {

        **updated,

        "tool_output": report,

        "final_response": report

    }


def body_node(state):

    report = body_agent.analyze_body(

        state["user_query"]

    )

    updated = memory_agent.store_body_metrics(

        state,

        report

    )

    return {

        **updated,

        "tool_output": report,

        "final_response": report

    }


def coach_node(state):

    answer = coach_agent.coach(

        state

    )

    return {

        "final_response": answer

    }