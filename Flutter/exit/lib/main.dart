import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Shazam',
      home: FirstTeb(),
    );
  }
}

class FirstTeb extends StatefulWidget {
  const FirstTeb({super.key});

  @override
  State<FirstTeb> createState() => _FirstTebState();
}

class _FirstTebState extends State<FirstTeb> {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Image.asset(
          'asset/instagram',
          width: 30,
          height: 30,
        ),
      ],
    );
  }
}
