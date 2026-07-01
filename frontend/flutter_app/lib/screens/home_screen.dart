import 'package:flutter/material.dart';

import '../response_widgets/response_renderer.dart';
import '../services/api_service.dart';
import '../widgets/chat_bubble.dart';
import '../widgets/message_input.dart';
import '../widgets/summary_card.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() =>
      _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final ApiService api = ApiService();

  final TextEditingController controller =
      TextEditingController();

  final ScrollController scrollController =
      ScrollController();

  bool loading = false;

  double calories = 0;

  double protein = 0;

  double burned = 0;

  final List<Map<String, dynamic>> messages = [
    {
      "isUser": false,
      "agent": "Coach Agent",
      "response":
          "👋 Welcome!\n\nI'll track it for u dont worry.\n\n🍽 Log Meals\n🏃 Track Workouts\n📊 Analyze Body\n💪 Get Fat Loss Advice\n\nStart typing below."
    }
  ];

  void scrollBottom() {
    Future.delayed(
      const Duration(milliseconds: 200),
      () {
        if (scrollController.hasClients) {
          scrollController.animateTo(
            scrollController.position.maxScrollExtent,
            duration:
                const Duration(milliseconds: 300),
            curve: Curves.easeOut,
          );
        }
      },
    );
  }

  Future<void> sendMessage() async {
    if (controller.text.trim().isEmpty) return;

    String userMessage = controller.text;

    controller.clear();

    setState(() {
      messages.add({
        "isUser": true,
        "text": userMessage,
      });

      loading = true;
    });

    scrollBottom();

    try {
      final result =
          await api.sendMessage(userMessage);

      setState(() {
        loading = false;

        calories =
            (result["summary"]["calories"] as num)
                .toDouble();

        protein =
            (result["summary"]["protein"] as num)
                .toDouble();

        burned =
            (result["summary"]["burned"] as num)
                .toDouble();

        messages.add({
          "isUser": false,
          "agent": result["agent"],
          "response": result["response"],
        });
      });

      scrollBottom();
    } catch (e) {
      setState(() {
        loading = false;

        messages.add({
          "isUser": false,
          "agent": "Coach Agent",
          "response": e.toString(),
        });
      });

      scrollBottom();
    }
  }


  Future<void> resetDay() async {
  try {
    await api.resetSession();

    setState(() {
      calories = 0;
      protein = 0;
      burned = 0;

      messages.clear();

      messages.add({
        "isUser": false,
        "agent": "Coach Agent",
        "response":
            "👋 Welcome!\n\nI'll track it for u dont worry.\n\n🍽 Log Meals\n🏃 Track Workouts\n📊 Analyze Body\n💪 Get Fat Loss Advice\n\nStart typing below."
      });
    });

    scrollBottom();

    if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text(
            "🚀 New Day Started Successfully!",
          ),
        ),
      );
    }
  } catch (e) {
    if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(
            e.toString(),
          ),
        ),
      );
    }
  }
}

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          "Application 54",
        ),
        actions: [
          IconButton(
            onPressed: () async {
  bool? reset = await showDialog(
    context: context,
    builder: (context) {
      return AlertDialog(
        title: const Text(
          "Reset Today's Progress",
        ),
        content: const Text(
          "This will clear all today's meals, workouts and summary.\n\nDo you want to continue?",
        ),
        actions: [
          TextButton(
            onPressed: () {
              Navigator.pop(
                context,
                false,
              );
            },
            child: const Text(
              "Cancel",
            ),
          ),
          ElevatedButton(
            onPressed: () {
              Navigator.pop(
                context,
                true,
              );
            },
            child: const Text(
              "Reset",
            ),
          ),
        ],
      );
    },
  );

  if (reset == true) {
    await resetDay();
  }
},
            icon: const Icon(
              Icons.refresh,
            ),
          )
        ],
      ),
      body: Column(
        children: [
          Padding(
            padding:
                const EdgeInsets.all(10),
            child: Row(
              children: [
                Expanded(
                  child: SummaryCard(
                    title: "Calories",
                    value:
                        "${calories.toStringAsFixed(0)} / 2200",
                    icon: Icons
                        .local_fire_department,
                  ),
                ),
                Expanded(
                  child: SummaryCard(
                    title: "Protein",
                    value:
                        "${protein.toStringAsFixed(1)} g",
                    icon: Icons.egg_alt,
                  ),
                ),
                Expanded(
                  child: SummaryCard(
                    title: "Burned",
                    value:
                        "${burned.toStringAsFixed(0)} kcal",
                    icon:
                        Icons.directions_run,
                  ),
                ),
              ],
            ),
          ),
          const Divider(),
          Expanded(
            child: ListView.builder(
              controller:
                  scrollController,
              itemCount: messages.length,
              itemBuilder:
                  (context, index) {
                final msg =
                    messages[index];

                if (msg["isUser"]) {
                  return ChatBubble(
                    message: msg["text"],
                    isUser: true,
                  );
                }

                return ResponseRenderer(
                  agent: msg["agent"],
                  response:
                      msg["response"],
                );
              },
            ),
          ),
          if (loading)
            const Padding(
              padding:
                  EdgeInsets.all(15),
              child: Row(
                children: [
                  CircularProgressIndicator(),
                  SizedBox(width: 15),
                  Text(
                    "🤖 am thinking bro just a sec...",
                    style: TextStyle(
                      fontSize: 16,
                    ),
                  )
                ],
              ),
            ),
          MessageInput(
            controller: controller,
            onSend: sendMessage,
          ),
        ],
      ),
    );
  }
}