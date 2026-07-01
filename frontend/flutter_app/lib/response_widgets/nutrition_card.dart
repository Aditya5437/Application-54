import 'package:flutter/material.dart';

class NutritionCard extends StatelessWidget {
  final Map data;

  const NutritionCard({
    super.key,
    required this.data,
  });

  Widget infoRow(
    String title,
    String value,
  ) {
    return Padding(
      padding: const EdgeInsets.symmetric(
        vertical: 4,
      ),
      child: Row(
        mainAxisAlignment:
            MainAxisAlignment.spaceBetween,
        children: [
          Text(
            title,
            style: const TextStyle(
              fontWeight: FontWeight.bold,
            ),
          ),
          Text(value),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final food = data["foods"][0];

    final total = data["total"];

    return Card(
      margin: const EdgeInsets.all(10),
      child: Padding(
        padding: const EdgeInsets.all(18),
        child: Column(
          crossAxisAlignment:
              CrossAxisAlignment.start,
          children: [

            const Text(
              "🍽 Meal Summary",
              style: TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 20),

            Text(
              "${food["food_name"]} (${food["quantity"]} ${food["unit"]})",
              style: const TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),

            const Divider(),

            infoRow(
              "🔥 Calories",
              "${food["calories"]}",
            ),

            infoRow(
              "🥩 Protein",
              "${food["protein"]} g",
            ),

            infoRow(
              "🍚 Carbs",
              "${food["carbs"]} g",
            ),

            infoRow(
              "🧈 Fat",
              "${food["fat"]} g",
            ),

            const SizedBox(height: 18),

            const Divider(),

            const Text(
              "TOTAL",
              style: TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 18,
              ),
            ),

            const SizedBox(height: 10),

            infoRow(
              "Calories",
              "${total["calories"]}",
            ),

            infoRow(
              "Protein",
              "${total["protein"]} g",
            ),

            infoRow(
              "Carbs",
              "${total["carbs"]} g",
            ),

            infoRow(
              "Fat",
              "${total["fat"]} g",
            ),
          ],
        ),
      ),
    );
  }
}