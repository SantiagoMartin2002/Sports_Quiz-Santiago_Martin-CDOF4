# Sports Quiz Game

## Overview
The Sports Quiz Game is an interactive Python application designed to test users' knowledge in various sports. Users can take a quiz consisting of multiple-choice questions, and their scores are recorded and ranked on a leaderboard.

## Features
User Registration: Users can enter their username to start the quiz.
Randomized Questions: Each quiz session randomly selects 5 questions from a pool of sports-related questions.
Scoring and Leaderboard: Scores are calculated based on correct answers. High scores are saved and ranked in a leaderboard, which updates only if the user achieves a new high score.
Leaderboard Ranking: Displays users' ranks based on their high scores in descending order.

## How to Run
Ensure Python 3 is installed on your system.
Download the project files to your local machine.
Run the script using a Python interpreter: python quiz.py

## Adding Questions
To add new questions to the quiz, edit the load_questions function in sports_quiz.py and follow the format: ("Question text", "Correct answer", ["Option1", "Option2", "Option3", "Option4"]).

## Leaderboard File
The leaderboard is stored in leaderboard.csv, where scores are persisted across game sessions.

## Dependencies
Python 3.x
No external libraries required

## Future Enhancements
Implement a GUI for a more interactive experience.
Extend the question bank and categorize questions by sports type.
Add difficulty levels and timed questions for added challenge.
