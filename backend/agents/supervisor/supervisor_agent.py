from backend.agents.base_agent import BaseAgent

from backend.prompts.system_prompt import SUPERVISOR_SYSTEM_PROMPT


class SupervisorAgent(BaseAgent):

    def __init__(self):

        super().__init__(SUPERVISOR_SYSTEM_PROMPT)

    def route(self, query: str):

        return self.invoke(query)