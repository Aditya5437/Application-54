import 'package:flutter/material.dart';

class AppTheme {

  static ThemeData darkTheme = ThemeData(

    brightness: Brightness.dark,

    useMaterial3: true,

    colorSchemeSeed: Colors.green,

    scaffoldBackgroundColor: const Color(0xFF101418),

    appBarTheme: const AppBarTheme(

      centerTitle: true,

      elevation: 0,

      backgroundColor: Color(0xFF101418),

    ),

    cardTheme: const CardThemeData(

      elevation: 4,

      margin: EdgeInsets.all(8),

    ),

  );

}