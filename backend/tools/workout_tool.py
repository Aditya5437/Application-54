class WorkoutTool:
    
    MET_VALUES = {

        "walking": 3.5,

        "running": 9.8,

        "cycling": 7.5,

        "strength training": 5.0,

        "yoga": 2.8,

        "swimming": 8.3

    }

    # Approximate calories burned per km per kg
    DISTANCE_FACTORS = {

        "walking": 0.75,

        "running": 1.03,

        "cycling": 0.30

    }

    # Approximate calories burned per step
    STEP_FACTORS = {

        "walking": 0.045,

        "running": 0.065

    }

    def calculate_calories(

        self,

        exercise,

        duration_minutes,

        body_weight,

        distance=0,

        distance_unit="",

        steps=0

    ):

        exercise = exercise.lower()

        # ------------------------
        # Priority 1
        # Duration + MET
        # ------------------------

        if duration_minutes > 0:

            met = self.MET_VALUES.get(

                exercise,

                4.0

            )

            calories = (

                met *

                body_weight *

                duration_minutes

            ) / 60

            return round(calories,2)

        # ------------------------
        # Priority 2
        # Distance
        # ------------------------

        if distance > 0:

            if distance_unit.lower() == "m":

                distance = distance / 1000

            factor = self.DISTANCE_FACTORS.get(

                exercise,

                0.75

            )

            calories = (

                factor *

                body_weight *

                distance

            )

            return round(calories,2)

        # ------------------------
        # Priority 3
        # Steps
        # ------------------------

        if steps > 0:

            factor = self.STEP_FACTORS.get(

                exercise,

                0.045

            )

            calories = (

                steps *

                factor

            )

            return round(calories,2)

        return 0