from pprint import pprint

from backend.agents.nutrition.nutrition_agent import NutritionAgent

agent = NutritionAgent()

query = """
Today I ate

250 ml milk

200 g paneer

2 bananas

10 g butter
"""

result = agent.process_meal(query)

pprint(result)