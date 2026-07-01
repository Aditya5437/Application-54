from backend.graph.initial_state import create_initial_state


class SessionManager:

    def __init__(self):

        self.state = create_initial_state("")

    def get_state(self):

        return self.state

    def update_state(self, new_state):

        self.state = new_state

    def set_query(self, query: str):

        self.state["user_query"] = query

    def reset(self):

        self.state = create_initial_state("")