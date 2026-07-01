import 'package:flutter/material.dart';

class CoachCard extends StatelessWidget {

  final String message;

  const CoachCard({

    super.key,

    required this.message,

  });

  @override
  Widget build(BuildContext context) {

    return Card(

      margin: const EdgeInsets.all(10),

      child: Padding(

        padding: const EdgeInsets.all(16),

        child: Text(

          message,

          style: const TextStyle(

            fontSize: 16,

          ),

        ),

      ),

    );

  }

}