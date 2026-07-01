from backend.tools.nutrition_tool import NutritionTool

tool = NutritionTool()

foods = [

    ("Paneer", 200),

    ("Milk", 250),

    ("Banana", 2)

]

for food_name, quantity in foods:

    print()

    result = tool.calculate_macros(

        food_name,

        quantity

    )

    print(result)