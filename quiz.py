#some random question for examples
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Kolkata"],
        "answer": "A"
    },
    {
        "question": "Which language is used for Data Science?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. JavaScript"],
        "answer": "B"
    },
    {
        "question": "What does OOP stand for?",
        "options": [
            "A. Object Oriented Programming",
            "B. Open Output Process",
            "C. Online Operation Program",
            "D. None"
        ],
        "answer": "A"
    }
]


score = 0

for q in questions:
    print("\n "+q['question'])

    for option in q['options']:
        print("\t"+option)

    user_answer = input("\nEnter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1

    else:
        print("Wrong!")

print("\n---- QUIZE IS COMPLETE ----")
print(f"Your final score is: {score}")

percentage = score/len(questions)*100
print(f"Your final percentage is: {percentage:.2f}%")