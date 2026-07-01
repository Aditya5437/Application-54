from backend.agents.supervisor.supervisor_agent import SupervisorAgent
agent = SupervisorAgent()

queries = [
     "I ate 200g paneer",

    "Generate my fat loss plan",

    "I walked 12000 steps",

    "Show yesterday meals"
]

for q in queries:
    print()
    print("USER :", q)
    print("ROUTE :", agent.route(q))
