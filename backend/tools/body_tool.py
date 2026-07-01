class BodyTool:
    
    def calculate_bmi(

        self,

        weight,

        height_cm

    ):

        height_m = height_cm / 100

        return round(

            weight / (height_m ** 2),

            2

        )

    def calculate_bmr(

        self,

        gender,

        weight,

        height,

        age

    ):

        if gender.lower() == "male":

            return round(

                (10 * weight)

                +

                (6.25 * height)

                -

                (5 * age)

                +

                5,

                2

            )

        return round(

            (10 * weight)

            +

            (6.25 * height)

            -

            (5 * age)

            -

            161,

            2

        )

    def calculate_tdee(

        self,

        bmr,

        activity_factor=1.55

    ):

        return round(

            bmr * activity_factor,

            2

        )

    def calculate_fat_loss_calories(

        self,

        tdee

    ):

        return round(

            tdee - 500,

            2

        )

    def calculate_macros(

        self,

        weight,

        calories

    ):

        protein = weight * 2.2

        fat = weight * 0.8

        protein_calories = protein * 4

        fat_calories = fat * 9

        carb_calories = calories - protein_calories - fat_calories

        carbs = carb_calories / 4

        return {

            "protein": round(protein,2),

            "fat": round(fat,2),

            "carbs": round(carbs,2)

        }