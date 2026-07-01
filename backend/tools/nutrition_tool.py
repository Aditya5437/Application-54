import requests

from backend.config.settings import settings


class NutritionTool:

    BASE_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"

    def __init__(self):
        self.api_key = settings.USDA_API_KEY

    def search_food(self, food_name: str):

        params = {
            "query": food_name,
            "pageSize": 1,
            "api_key": self.api_key
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=20
        )

        if response.status_code != 200:
            return None

        foods = response.json().get("foods", [])

        if not foods:
            return None

        food = foods[0]

        nutrients = {}

        for nutrient in food.get("foodNutrients", []):

            nutrients[nutrient.get("nutrientName")] = nutrient.get("value")

        # Try to determine serving information
        food_portions = food.get("foodPortions", [])

        per_quantity = 100
        per_unit = "g"

        if food_portions:

            portion = food_portions[0]

            if portion.get("gramWeight"):
                per_quantity = portion.get("gramWeight")

            if portion.get("modifier"):
                per_unit = portion.get("modifier")

        return {

            "food_name": food.get("description"),

            "per_quantity": per_quantity,

            "per_unit": per_unit,

            "calories": nutrients.get("Energy"),

            "protein": nutrients.get("Protein"),

            "carbs": nutrients.get("Carbohydrate, by difference"),

            "fat": nutrients.get("Total lipid (fat)")
        }

    def calculate_macros(
        self,
        food_name: str,
        quantity: float,
        unit: str
    ):

        food = self.search_food(food_name)

        if food is None:
            return None

        input_unit = unit.lower()

        # Weight / Volume based foods
        if input_unit in ["g", "gram", "grams", "ml"]:

            multiplier = quantity / food["per_quantity"]

        else:
            # count, slice, piece, etc.
            multiplier = quantity

        return {

            "food_name": food["food_name"],

            "quantity": quantity,

            "unit": unit,

            "calories": round(food["calories"] * multiplier, 2),

            "protein": round(food["protein"] * multiplier, 2),

            "carbs": round(food["carbs"] * multiplier, 2),

            "fat": round(food["fat"] * multiplier, 2)

        }