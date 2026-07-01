import 'package:flutter/material.dart';

import 'config/app_theme.dart';

import 'screens/home_screen.dart';

void main() {

  runApp(

    const FatLossAgentApp(),

  );

}

class FatLossAgentApp extends StatelessWidget {

  const FatLossAgentApp({super.key});

  @override
  Widget build(BuildContext context) {

    return MaterialApp(

      debugShowCheckedModeBanner: false,

      title: "Fat Loss AI",

      theme: AppTheme.darkTheme,

      home: const HomeScreen(),

    );

  }

}