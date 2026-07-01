from backend.tools.nutrition_tool import NutritionTool

tool = NutritionTool()
food = tool.search_food("Paneer")
print(food)