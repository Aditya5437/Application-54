import json

from backend.agents.base_agent import BaseAgent

from backend.prompts.nutrition_prompt import NUTRITION_SYSTEM_PROMPT

from backend.tools.nutrition_tool import NutritionTool


class NutritionAgent(BaseAgent):

    def __init__(self):

        super().__init__(NUTRITION_SYSTEM_PROMPT)

        self.tool = NutritionTool()

    def process_meal(self, query: str):

        response = self.invoke(query)

        food_items = json.loads(response)

        nutrition_results = []

        total = {

            "calories": 0,

            "protein": 0,

            "carbs": 0,

            "fat": 0

        }

        for item in food_items:

            result = self.tool.calculate_macros(

                food_name=item["food_name"],

                quantity=item["quantity"],

                unit=item["unit"]

            )

            if result:

                nutrition_results.append(result)

                total["calories"] += result["calories"]

                total["protein"] += result["protein"]

                total["carbs"] += result["carbs"]

                total["fat"] += result["fat"]

        return {

            "foods": nutrition_results,

            "total": {

                "calories": round(total["calories"], 2),

                "protein": round(total["protein"], 2),

                "carbs": round(total["carbs"], 2),

                "fat": round(total["fat"], 2)

            }

        }