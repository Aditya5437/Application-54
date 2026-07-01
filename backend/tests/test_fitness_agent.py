from pprint import pprint

from backend.agents.fitness.fitness_agent import FitnessAgent

agent = FitnessAgent()

query = """
Today I walked 7 km in 90 minutes.
"""

result = agent.process_workout(

    query,

    body_weight=73

)

pprint(result)