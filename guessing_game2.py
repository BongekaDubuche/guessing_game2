from random import randint
Easy = 5
Hard = 10

def check_answer(guess, answer, turns):
    while answer != guess:
        if answer > guess:
            print("Too High")
            return turns -1
        elif answer < guess:
            print("Too Low")
            return turns -1
        else:
            print(f"You got it the answer is{answer}")


def set_level():
    game = input("What level do you want to play? 'Easy' or 'Hard \n")
    if game == 'Easy':
        return Easy
    else:
        return Hard


def game():
    print("Welcome to guessing game! ")
    print("I'm thinking of the number. ")
    answer = randint(1, 100)
    print(f"The correct answer is {answer}")
     
    turns = set_level
    guess = 0 

    while answer != guess:
        print(f"You have {turns} attempts remaining to guess the answer ")
        guess = int(input("Guess the number 1 and 100. \n"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've have run out of guess. you lose.")
            return
        elif answer != guess:
            print("Guess again. ")

game()
