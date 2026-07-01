from pprint import pprint

from backend.agents.memory.memory_agent import MemoryAgent

from backend.graph.initial_state import create_initial_state


memory = MemoryAgent()

state = create_initial_state("")


nutrition_report = {

    "foods":[

        {

            "food_name":"Paneer",

            "quantity":200,

            "unit":"g",

            "calories":620,

            "protein":42,

            "carbs":7,

            "fat":48

        }

    ],

    "total":{

        "calories":620,

        "protein":42,

        "carbs":7,

        "fat":48

    }

}


state.update(

    memory.store_meal(

        state,

        nutrition_report

    )

)

print()

print("Meal History")

pprint(

    memory.get_meal_history(

        state

    )

)

print()

print("Daily Totals")

pprint(

    memory.get_daily_totals(

        state

    )

)