# python quiz name:
questions = ("How many elements are there in a periodic Table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abudant gas in the atmosphere?: ",
             "How many bones are there in the human body?: ",
             "Which is the hottest planet in the solar system?: ")
options = (("A. 116", "B. 117", "C. 118","D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant","D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide","D. Hydrogen"),
           ("A. 206", "B. 207 ", "C. 208","D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth","D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
questionNum = 0

for question in questions:
    print("--------------------------------------------------------")
    print(question)
    for option in options[questionNum]:
        print(option)

    guess = input("Enter your answer option between: A, B, C, D: ").upper()
    guesses.append(guess)
    if guess == answers[questionNum]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[questionNum]} was the correct answer! ")
    questionNum += 1

print("------------------------------------------------")
print("----------------RESULTS--------------------------")
print("-------------------------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"Your final score is {score}%")




