class MemoryAgent:
    
    def store_meal(
        self,
        state,
        nutrition_report
    ):

        meals = state["meal_history"]

        meals.extend(
            nutrition_report["foods"]
        )

        totals = state["daily_totals"]

        totals["calories"] += nutrition_report["total"]["calories"]
        totals["protein"] += nutrition_report["total"]["protein"]
        totals["carbs"] += nutrition_report["total"]["carbs"]
        totals["fat"] += nutrition_report["total"]["fat"]

        return {

            "meal_history": meals,

            "daily_totals": totals

        }

    def store_workout(
        self,
        state,
        workout_report
    ):

        workouts = state["workout_history"]

        workouts.append(workout_report)

        return {

            "workout_history": workouts

        }

    def store_body_metrics(
        self,
        state,
        body_report
    ):

        return {

            "body_metrics": body_report

        }

    def get_daily_totals(
        self,
        state
    ):

        return state["daily_totals"]

    def get_meal_history(
        self,
        state
    ):

        return state["meal_history"]

    def get_workout_history(
        self,
        state
    ):

        return state["workout_history"]

    def get_body_metrics(
        self,
        state
    ):

        return state["body_metrics"]

    def clear_memory(
        self,
        state
    ):

        return {

            "meal_history": [],

            "workout_history": [],

            "body_metrics": {},

            "daily_totals": {

                "calories": 0,

                "protein": 0,

                "carbs": 0,

                "fat": 0

            }

        }