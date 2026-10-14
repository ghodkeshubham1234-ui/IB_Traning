import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Questions, options, and answers
questions = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A: Venus", "B: Mars", "C: Jupiter", "D: Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote the Indian national anthem Jana Gana Mana?",
        "options": ["A: Rabindranath Tagore", "B: Bankim Chandra Chatterjee", "C: Mahatma Gandhi", "D: Subhash Chandra Bose"],
        "answer": "A"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["A: Sydney", "B: Melbourne", "C: Canberra", "D: Perth"],
        "answer": "C"
    },
    {
        "question": "Which is the largest organ in the human body?",
        "options": ["A: Heart", "B: Liver", "C: Skin", "D: Brain"],
        "answer": "C"
    },
    {
        "question": "Who was the first woman Prime Minister of India?",
        "options": ["A: Sonia Gandhi", "B: Indira Gandhi", "C: Sarojini Naidu", "D: Pratibha Patil"],
        "answer": "B"
    }
]

# Game loop
score = 0
engine.say("Welcome to Kaun Banega Crorepati!")
engine.runAndWait()

for i, q in enumerate(questions, 1):
    print(f"\nQuestion {i}: {q['question']}")
    engine.say(f"Question {i}: {q['question']}")
    for opt in q["options"]:
        print(opt)
        engine.say(opt)
    engine.runAndWait()

    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("Correct Answer! 🎉")
        engine.say("Correct Answer! is ")
        score += 1
    else:
        print("Wrong Answer ❌")
        engine.say("Wrong Answer")
    engine.runAndWait()

print(f"\nGame Over! Your final score is {score} out of {len(questions)}")
engine.say(f"Game Over! Your final score is {score} out of {len(questions)}")
engine.runAndWait()
