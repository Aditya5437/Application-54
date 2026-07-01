import 'package:flutter/material.dart';

class BodyCard extends StatelessWidget {
  final Map data;

  const BodyCard({
    super.key,
    required this.data,
  });

  Widget row(String title, String value) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 6),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
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
    return Card(
      margin: const EdgeInsets.all(10),
      child: Padding(
        padding: const EdgeInsets.all(18),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [

            const Text(
              "📊 Body Analysis",
              style: TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.bold,
              ),
            ),

            const Divider(),

            row("⚖ Weight", "${data["weight"]} kg"),

            row("📏 Height", "${data["height"]} cm"),

            row("🧈 Body Fat", "${data["body_fat"]}%"),

            row("📈 BMI", data["bmi"].toString()),

            row("🔥 BMR", "${data["bmr"]} kcal"),

            row("⚡ TDEE", "${data["tdee"]} kcal"),

            row("🎯 Target Calories",
                "${data["target_calories"]} kcal"),
          ],
        ),
      ),
    );
  }
}