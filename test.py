import pygame
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG!")
        return 0

#-------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
    if score < 80:
        print("Cmon, The questions werent")


#-------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
#-------------------------


questions = {"What year was Python created?: ": "B",
 "Is the Earth round?: ": "A",
 "What does GPU stand for?: ": "C"
 "Python is atributed to which comedy group?: ": "C",
 "Who created Python?: ": "A",
"": "",
"": "",
"": "",
"": "",
"": "",
"": "",
"": "",
"": "",
"": "",
"": "",
"": "",
"": "",
"": "",
"": "",
"": "",
}

options = [["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"],A
          ["A. Game Processing Unit", "B. Grand Processing Unit", "C. Graphics Processing Unit", "D. Gray Proccessing Unit"]
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          [""],
          [""],
          [""],
          [""],
          [""],
          [""],
          [""],
          [""],
          [""],
          [""],
          [""],
          [""],
          [""],
          [""],
          [""],
          ]


new_game()

while play_again():
    new_game()

print("Byeeeeee!")