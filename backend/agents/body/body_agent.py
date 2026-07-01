import json

from backend.agents.base_agent import BaseAgent

from backend.prompts.body_prompt import BODY_SYSTEM_PROMPT

from backend.tools.body_tool import BodyTool


class BodyAgent(BaseAgent):

    def __init__(self):

        super().__init__(BODY_SYSTEM_PROMPT)

        self.tool = BodyTool()

    def analyze_body(

        self,

        query

    ):

        body = json.loads(

            self.invoke(query)

        )

        bmi = self.tool.calculate_bmi(

            body["weight"],

            body["height"]

        )

        bmr = self.tool.calculate_bmr(

            body["gender"],

            body["weight"],

            body["height"],

            body["age"]

        )

        tdee = self.tool.calculate_tdee(

            bmr

        )

        fat_loss = self.tool.calculate_fat_loss_calories(

            tdee

        )

        macros = self.tool.calculate_macros(

            body["weight"],

            fat_loss

        )

        body["bmi"] = bmi

        body["bmr"] = bmr

        body["tdee"] = tdee

        body["fat_loss_calories"] = fat_loss

        body["macro_targets"] = macros

        return body