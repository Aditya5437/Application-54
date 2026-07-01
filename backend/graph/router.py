def route_agent(state):
    
    agent = state["agent_name"]

    if agent == "Nutrition Agent":
        return "nutrition"

    elif agent == "Fitness Agent":
        return "fitness"

    elif agent == "Body Agent":
        return "body"

    elif agent == "Coach Agent":
        return "coach"

    return "coach"