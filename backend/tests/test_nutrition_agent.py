from backend.agents.nutrition.nutrition_agent import NutritionAgent


agent = NutritionAgent()

query = """
Today I ate

250 ml Chitale milk

200 grams paneer

2 bananas

1 jowar bhakri

10 grams butter
"""

foods = agent.extract_food_items(query)

print()

for item in foods:

    print(item)