from backend.agents.base_agent import BaseAgent

from backend.prompts.coach_prompt import COACH_SYSTEM_PROMPT


class CoachAgent(BaseAgent):

    def __init__(self):

        super().__init__(COACH_SYSTEM_PROMPT)

    def coach(self, state):

        prompt = f"""
Current Session

Body Metrics

{state["body_metrics"]}


Daily Totals

{state["daily_totals"]}


Meal History

{state["meal_history"]}


Workout History

{state["workout_history"]}


User Question

{state["user_query"]}
"""

        return self.invoke(prompt)