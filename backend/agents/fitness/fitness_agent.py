import json

from backend.agents.base_agent import BaseAgent

from backend.prompts.fitness_prompt import FITNESS_SYSTEM_PROMPT

from backend.tools.workout_tool import WorkoutTool


class FitnessAgent(BaseAgent):

    def __init__(self):

        super().__init__(FITNESS_SYSTEM_PROMPT)

        self.tool = WorkoutTool()

    def process_workout(

        self,

        query,

        body_weight=70

    ):

        workout = json.loads(

            self.invoke(query)

        )

        calories = self.tool.calculate_calories(
            exercise=workout["exercise"],

            duration_minutes=workout["duration"],

            body_weight=body_weight,

            distance=workout["distance"],

            distance_unit=workout["distance_unit"],

            steps=workout["steps"]
            
        )

        workout["calories_burned"] = calories

        return workout