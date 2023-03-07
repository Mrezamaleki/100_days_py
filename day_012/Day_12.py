from random import randint

def check_answer(guess, number, turn):
    if guess > number:
        print("Too high.")
        turn -= 1
    elif guess < number:
        print("Too low.")
        turn -= 1
    else:
        print(f"You got it! The answer was {number}.")
        win = True
    return turn

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 100)
    print(number)
    type = input("Choose a difficulty. Type 'easy' or 'hard':")
    if type == 'easy':
        turn = 10
    else:
        turn = 5
    guess = 0
    while guess != number:
        print(f"You have {turn} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turn = check_answer(guess, number, turn)
        if turn == 0:
          print("You've run out of guesses, you lose.")
          return
        elif guess != number:
            print("Guess again.")

game()
