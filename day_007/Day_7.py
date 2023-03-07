from replit import clear
from hangman_words import word_list
# word_list = ["ardvark", "baboon", "camel"]

from hangman_art import logo
print(logo)

import random
# a = 0
# b = 0
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)
answer = []

for i in range(len(chosen_word)):
    answer += "_"

# print(answer)

end_of_game = False
# correct_answer = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    # a += 1
    if guess in answer:
        print(f"You've already guessed {guess}")

    for i in range(len(answer)):
        if chosen_word[i] == guess:
            answer[i] = guess
            # correct_answer = True

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # print(answer)

    # if correct_answer:
    #     b += 1
    #     correct_answer = False

    elif "_" not in answer:
        print("You win.")

    # elif a - b == 7:
    #     end_of_game = True
    #     print("You lost.")

    # print(a, b)
    # print(stages[6-a+b])
    from hangman_art import stages
    print(stages[lives])