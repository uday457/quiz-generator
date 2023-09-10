# Define a list of questions, options, and correct answers
questions = [
    {
        "question": "What is the capital of india?",
        "options": ["A) Ap", "B) Ts", "C) Delhi", "D) Pune"],
        "correct_answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "correct_answer": "B"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Rhinoceros"],
        "correct_answer": "B"
    }
]

# Function to display a question and its options
def ask_question(question_dict):
    print(question_dict["question"])
    for option in question_dict["options"]:
        print(option)
    user_answer = input("Enter the letter of your answer (A, B, C, or D): ").upper()
    return user_answer

# Function to check if the user's answer is correct
def check_answer(question_dict, user_answer):
    return user_answer == question_dict["correct_answer"]

# Main quiz loop
score = 0
for question in questions:
    user_choice = ask_question(question)
    if check_answer(question, user_choice):
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

# Display the final score
print(f"Quiz completed! Your score: {score}/{len(questions)}")