import 'package:flutter/material.dart';

class FitnessCard extends StatelessWidget {

  final Map data;

  const FitnessCard({

    super.key,

    required this.data,

  });

  Widget row(

      String title,

      String value

  ){

    return Padding(

      padding: const EdgeInsets.symmetric(

        vertical:6,

      ),

      child: Row(

        mainAxisAlignment:

            MainAxisAlignment.spaceBetween,

        children:[

          Text(

            title,

            style: const TextStyle(

              fontWeight: FontWeight.bold,

            ),

          ),

          Text(value)

        ],

      ),

    );

  }

  @override
  Widget build(BuildContext context){

    return Card(

      margin: const EdgeInsets.all(10),

      child: Padding(

        padding: const EdgeInsets.all(16),

        child: Column(

          crossAxisAlignment:

              CrossAxisAlignment.start,

          children:[

            const Text(

              "🏃 Workout Summary",

              style: TextStyle(

                fontSize:20,

                fontWeight: FontWeight.bold,

              ),

            ),

            const SizedBox(height:15),

            row(

              "Exercise",

              data["exercise"],

            ),

            row(

              "Distance",

              "${data["distance"]} ${data["distance_unit"]}",

            ),

            row(

              "Duration",

              "${data["duration"]} ${data["duration_unit"]}",

            ),

            row(

              "Calories",

              "${data["calories_burned"]} kcal",

            ),

          ],

        ),

      ),

    );

  }

}