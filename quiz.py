import random
import csv
import os

# This function contains the question bank for the quiz
def load_questions():
    questions = [
    ("In which year were the first modern Olympic Games held?", "1896", ["1896", "1900", "1912", "1924"]),
    ("Which country won the 2018 FIFA World Cup?", "France", ["Brazil", "Germany", "France", "Argentina"]),
    ("What sport is known as 'the sport of kings'?", "Horse Racing", ["Golf", "Polo", "Horse Racing", "Tennis"]),
    ("Who is often called the 'King of Clay' in the tennis world?", "Rafael Nadal", ["Roger Federer", "Novak Djokovic", "Rafael Nadal", "Andy Murray"]),
    ("In basketball, how many points is a shot made from beyond the three-point line worth?", "3", ["2", "3", "4", "5"]),
    ("What is the highest score possible in a single frame of ten-pin bowling?", "30", ["10", "15", "30", "60"]),
    ("Which country hosted the 2016 Summer Olympics?", "Brazil", ["China", "Brazil", "Russia", "Japan"]),
    ("In which sport would you perform the Fosbury Flop?", "High Jump", ["Pole Vault", "Diving", "High Jump", "Triple Jump"]),
    ("What is the national sport of Japan?", "Sumo Wrestling", ["Baseball", "Judo", "Sumo Wrestling", "Karate"]),
    ("Who holds the record for the most goals in a single Premier League season?", "Mohamed Salah", ["Alan Shearer", "Cristiano Ronaldo", "Mohamed Salah", "Harry Kane"])
    ]
    return questions

# Function to conduct the quiz
def conduct_quiz(questions):
    random.shuffle(questions)
    score = 0

    for i in range(5):
        question, correct_answer, options = questions[i]
        print(f"Q{i+1}: {question}")
        for idx, option in enumerate(options):
            print(f"{idx+1}. {option}")
        answer = input("Your answer (1-4): ")

        if options[int(answer)-1] == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}")

    return score

# Function to update the leaderboard
def update_leaderboard(username, score):
    leaderboard_file = 'leaderboard.csv'
    leaderboard = {}

    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                leaderboard[row[0]] = int(row[1])

    if username in leaderboard:
        if score > leaderboard[username]:
            leaderboard[username] = score
    else:
        leaderboard[username] = score

    with open(leaderboard_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "Score"])
        for user, score in leaderboard.items():
            writer.writerow([user, score])

# Function to display the leaderboard
def display_leaderboard():
    leaderboard_file = 'leaderboard.csv'

    if not os.path.exists(leaderboard_file):
        print("No leaderboard data available.")
        return

    leaderboard = []
    with open(leaderboard_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            leaderboard.append((row[0], int(row[1])))

    leaderboard.sort(key=lambda x: x[1], reverse=True)

    print("Leaderboard:")
    for rank, (user, score) in enumerate(leaderboard, start=1):
        print(f"{rank}. {user} - {score}")

# Main function to start the quiz game
def start_quiz():
    username = input("Enter your username: ")
    questions = load_questions()
    score = conduct_quiz(questions)
    update_leaderboard(username, score)
    print(f"Your score: {score}/5")
    display_leaderboard()

# Start the game
start_quiz()