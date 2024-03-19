print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "Who wrote 'Romeo and Juliet'?", "answer": "Shakespeare"},
        {"question": "What is the chemical symbol for water?", "answer": "H2O"},
        {"question":"Which is the only vowel on a standard keyboard that is not on the top line of letters?","answer":"A"},
        {"question": "Which American state is the largest (by area)?", "answer": "Alaska"}
    ]
score = 0
for q in questions:
    print(q["question"])
    user_answer = input("Your answer: ")
    if user_answer.lower() == q["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
print("You got", score, "out of", len(questions), "questions correct!")
print("You got " + str((score / len(questions)) * 100) + "%.")