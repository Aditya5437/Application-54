from pprint import pprint

from backend.agents.body.body_agent import BodyAgent

agent = BodyAgent()

query = """
I am 24 years old

Male

176 cm

76 kg

22 percent body fat

I want fat loss.
"""

result = agent.analyze_body(

    query

)

pprint(result)