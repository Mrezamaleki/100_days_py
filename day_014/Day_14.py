from game_data import data
from art import logo, vs
import random
from replit import clear

def account_data(account):
    name_account = account["name"]
    description_account = account["description"]
    country_account = account["country"]
    return (f"{name_account}, a {description_account}, from {country_account}")

print(logo)
score = 0
stop_game = False

def account():
    first = random.choice(data)
    second = random.choice(data)
    if first == second:
        second = random.choice(data)
    return first, second

first_account, second_account = account()

def new_account(first):
    second = random.choice(data)
    if first == second:
        second = random.choice(data)
    return second

while not stop_game:

    print(f"Compare A: {account_data(first_account)}")
    print(vs)
    print(f"Compare B: {account_data(second_account)}")

    # Ask user for a guess.
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # Check if user is correct.
    first_account_follower = first_account["follower_count"]
    second_account_follower = second_account["follower_count"]
    if user_guess == "a" and first_account_follower > second_account_follower:
        score += 1
        print(f"You're right! Current score: {score}.")
        clear()
        second_account = new_account(first_account)

    elif user_guess == "b" and second_account_follower > first_account_follower:
        score += 1
        print(f"You're right! Current score: {score}.")
        clear()
        first_account = second_account
        second_account = new_account(first_account)
    else:
        print(f"Sorry, that's wrong. Final score:{score}.")
        stop_game = True

# Making account at position B become the next account at position A.

# Clear the screen between rounds.
