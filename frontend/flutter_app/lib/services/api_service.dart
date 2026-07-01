import 'dart:convert';

import 'package:http/http.dart' as http;

import '../constants/api_constants.dart';

class ApiService {
  Future<Map<String, dynamic>> sendMessage(
      String message) async {
    final response = await http.post(
      Uri.parse(
        ApiConstants.baseUrl +
            ApiConstants.chatEndpoint,
      ),
      headers: {
        "Content-Type": "application/json",
      },
      body: jsonEncode({
        "message": message,
      }),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    }

    throw Exception("Unable to connect to backend.");
  }

  Future<void> resetSession() async {
    final response = await http.post(
      Uri.parse(
        ApiConstants.baseUrl +
            ApiConstants.resetEndpoint,
      ),
    );

    if (response.statusCode != 200) {
      throw Exception(
        "Unable to reset session.",
      );
    }
  }
}