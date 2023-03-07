import random

# random_integer = random.randint(1, 10)
# print(random_integer)
#
# random_float = random.random() * 5
# print(random_float)
#
# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

#Exercise 1
# Remember to use the random module
# import random
#
# rand_integer = random.randint(0, 1)
# if rand_integer == 1:
#     print("Heads")
# else:
#     print("Tails")
#
# list = ["House", "Window", "Door"]
# print(list[0], list[2])
#
# list.append("Apartment")
#
# print(list)

# Exercise 2
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

l = len(names)

index = random.randint(0, l)

print(f"{names[index]} is going to buy the meal today!")

# Exercise 3-Treasure Map

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
position_str = str(position)
if int(position_str[-1]) == 1:
    row1[int(position_str[-2])-1] = "X"
elif int(position_str[-1]) == 2:
    row2[int(position_str[-2])-1] = "X"
else:
    row3[int(position_str[-2])-1] = "X"

horizontal = int(position[0])
vertical = int(position[1])
map[vertical - 1][horizontal -1] = "X"

print(f"{row1}\n{row2}\n{row3}")


#rock, paper, scissors
# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You Win!")
    elif user_choice == computer_choice:
        print("It's a draw")