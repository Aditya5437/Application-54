from abc import ABC
from langchain_core.messages import HumanMessage, SystemMessage
from backend.services.groq_service import llm

class BaseAgent(ABC):
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt
        self.llm = llm

    def invoke(self, query:str)->str:
        response = self.llm.invoke(
            [
                SystemMessage(content=self.system_prompt),
                HumanMessage(content=query)
            ]
        )
        return response.content.strip()
