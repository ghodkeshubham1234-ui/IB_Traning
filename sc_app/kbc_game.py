import pyttsx3
import time
import random


# ==========================================
# 1. VOICE FUNCTION - WORKING CONFIGURATION
# ==========================================

def speak(text):
    print("\nKBC:", text, flush=True)

    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)

    # Select the first installed voice
    voices = engine.getProperty("voices")
    if voices:
        engine.setProperty("voice", voices[0].id)

    engine.say(text)
    engine.runAndWait()
    engine.stop()

    time.sleep(0.3)


# ==========================================
# 2. QUESTIONS AND ANSWERS
# ==========================================


questions = [
    {
        "question": "Which is the largest planet in our solar system?",
        "options": ["Earth", "Saturn", "Jupiter", "Mars"],
        "answer": "C",
        "prize": 1000
    },
    {
        "question": "Who is known as the Father of the Indian Constitution?",
        "options": [
            "Mahatma Gandhi",
            "Dr. B. R. Ambedkar",
            "Jawaharlal Nehru",
            "Sardar Patel"
        ],
        "answer": "B",
        "prize": 2000
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "define", "fun", "def"],
        "answer": "D",
        "prize": 5000
    },
    {
        "question": "What is the capital of Maharashtra?",
        "options": ["Pune", "Nagpur", "Mumbai", "Nashik"],
        "answer": "C",
        "prize": 10000
    },
    {
        "question": "Which library is mainly used for numerical computing in Python?",
        "options": ["NumPy", "Flask", "Django", "Seaborn"],
        "answer": "A",
        "prize": 20000
    },
    {
        "question": "How many bits are there in one byte?",
        "options": ["4", "8", "16", "32"],
        "answer": "B",
        "prize": 40000
    },
    {
        "question": "Which SQL command is used to add new records to a table?",
        "options": ["UPDATE", "SELECT", "INSERT", "DELETE"],
        "answer": "C",
        "prize": 80000
    },
    {
        "question": "Which algorithm is commonly used for classification in machine learning?",
        "options": [
            "Linear Regression",
            "K-Means only",
            "Apriori",
            "Decision Tree"
        ],
        "answer": "D",
        "prize": 160000
    },
    {
        "question": "Which data structure follows the FIFO principle?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "B",
        "prize": 320000
    },
    {
        "question": "What does AI stand for?",
        "options": [
            "Automated Internet",
            "Advanced Information",
            "Artificial Intelligence",
            "Algorithm Integration"
        ],
        "answer": "C",
        "prize": 1000000
    }
]



# ==========================================
# 3. DISPLAY OPTIONS
# ==========================================

def display_options(options):
    for i, option in enumerate(options):
        letter = chr(65 + i)
        print(f"  {letter}. {option}")


# ==========================================
# 4. 50:50 LIFELINE
# ==========================================

def use_fifty_fifty(question):
    correct_answer = question["answer"]

    incorrect_answers = [
        letter
        for letter in ["A", "B", "C", "D"]
        if letter != correct_answer
    ]

    # Keep the correct answer and one wrong answer
    remaining = [correct_answer, random.choice(incorrect_answers)]
    random.shuffle(remaining)

    speak("Your 50:50 lifeline is activated.")
    print("\nRemaining options:")

    for letter in ["A", "B", "C", "D"]:
        if letter in remaining:
            index = ord(letter) - ord("A")
            print(f"  {letter}. {question['options'][index]}")
        else:
            print(f"  {letter}. Removed")


# ==========================================
# 5. MAIN GAME
# ==========================================

def play_kbc():
    score = 0
    lifeline_available = True

    speak("Welcome to Kaun Banega Crorepati!")
    speak("Let's start the game. Good luck!")
    speak("Enter A, B, C or D to answer.")
    speak("Enter L to use your 50:50 lifeline.")
    speak("Enter Q if you want to quit.")

    for number, question in enumerate(questions, start=1):

        print("\n" + "=" * 55)
        print(f"QUESTION {number} OF {len(questions)}")
        print(f"Prize money: Rs. {question['prize']:,}")
        print("=" * 55)

        # Speak question
        speak(question["question"])

        # Display and speak options
        display_options(question["options"])

        for i, option in enumerate(question["options"]):
            letter = chr(65 + i)
            speak(f"Option {letter}: {option}")

        # Get user's answer
        while True:
            answer = input(
                "\nEnter A/B/C/D, L for lifeline, "
                "or Q to quit: "
            ).strip().upper()

            if answer == "Q":
                speak("You have decided to quit the game.")
                break

            if answer == "L":
                if not lifeline_available:
                    speak("Sorry, your lifeline has already been used.")
                    continue

                use_fifty_fifty(question)
                lifeline_available = False
                continue

            if answer in ["A", "B", "C", "D"]:
                break

            print("Invalid input! Enter A, B, C, D, L or Q.")

        if answer == "Q":
            break

        # Check the answer
        if answer == question["answer"]:
            score = question["prize"]

            speak("Congratulations! Your answer is correct.")
            speak(f"You have won {question['prize']} rupees.")

            print(f"\nCurrent winnings: Rs. {score:,}")

            if number < len(questions):
                speak("Let's move to the next question.")

        else:
            correct_letter = question["answer"]
            correct_index = ord(correct_letter) - ord("A")
            correct_option = question["options"][correct_index]

            speak("Sorry! Your answer is incorrect.")
            speak(
                f"The correct answer is option "
                f"{correct_letter}, {correct_option}."
            )
            break

    # ======================================
    # 6. FINAL RESULT
    # ======================================

    print("\n" + "=" * 55)
    print("                 GAME OVER")
    print("=" * 55)
    print(f"Your final winnings: Rs. {score:,}")
    print("=" * 55)

    speak(f"Game over! Your final winnings are {score} rupees.")

    if score == questions[-1]["prize"]:
        speak("Excellent! You completed all the questions.")
    else:
        speak("Thank you for playing KBC. Goodbye!")


# ==========================================
# 7. RUN THE GAME
# ==========================================

if __name__ == "__main__":
    try:
        play_kbc()
    except KeyboardInterrupt:
        print("\nGame stopped by the user.")