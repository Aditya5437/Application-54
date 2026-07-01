import 'package:flutter/material.dart';

import 'body_card.dart';
import 'coach_card.dart';
import 'fitness_card.dart';
import 'nutrition_card.dart';

class ResponseRenderer extends StatelessWidget {
  final String agent;
  final dynamic response;

  const ResponseRenderer({
    super.key,
    required this.agent,
    required this.response,
  });

  @override
  Widget build(BuildContext context) {
    switch (agent) {
      case "Nutrition Agent":
        return NutritionCard(data: response);

      case "Fitness Agent":
        return FitnessCard(data: response);

      case "Body Agent":
        return BodyCard(data: response);

      case "Coach Agent":
        return CoachCard(message: response);

      default:
        return CoachCard(
          message: response.toString(),
        );
    }
  }
}