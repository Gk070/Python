# A Quiz Game

questions = ("1. What is an operating system?",
             "2. What is the main function of the command interpreter?",
             "3. In Operating Systems, which of the following is/are CPU scheduling algorithms?",
             "4. To access the services of the operating system, the interface is provided by the ___________",
             "5. CPU scheduling is the basis of ___________")

options = (("a) interface between the hardware and application programs", "b) collection of programs that manages hardware resources", "c) system service provider to the application programs", "d) all of the mentioned"),
           ("a) to provide the interface between the API and application program", "b) to handle the files in the operating system", "c) to get and execute the next user-specified command", "d) none of the mentioned"),
           ("a) Priority", "b) Round Robin", "c) Shortest Job First", "d) All of the mentioned"),
           ("a) Library", "b) System calls", "c) Assembly instructions", "d) API"),
           ("a) multiprogramming operating systems", "b) larger memory sized systems", "c) multiprocessor systems", "d) none of the mentioned"))

answers = ("d", "c", "d", "b", "a")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------------------------------------------------------------------------------")
    print()
    print(question)
    print()
    for option in options[question_num]:
        print(option)
    guess = input("Enter your answer: ").lower()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("Answer is Correct ✅")
        score += 1
    else:
        print("Answer is Incorrect ❌")
    question_num += 1
    print()

print()
print("Result")
print("--------------")
print(f"Correct Answers: {answers}")
print(f"Your Answers: {guesses}")
print(f"Total score is: {score} / 5")