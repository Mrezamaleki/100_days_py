# # Data types
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
#
# #Excersize 1
#
# number = int(input("Which number do you want to check? "))
#
# number = number % 2
#
# if number == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")
#
# #------------------------------------
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
#
#     # ------------------------------------
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
#
# # Excersize 2
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# BMI = float(weight)/(float(height)**2)
# B = round(float(weight)/(float(height)**2))
# if BMI < 18.5:
#     print(f"Your BMI is {B}, you are underweight.")
# elif 18.5 <= BMI < 25:
#     print(f"Your BMI is {B}, you have a normal weight.")
# elif 25 <= BMI < 30:
#     print(f"Your BMI is {B}, you are slightly overweight.")
# elif 30 <= BMI < 35:
#     print(f"Your BMI is {B}, you are obese.")
# else:
#     print(f"Your BMI is {B}, you are clinically obese.")
#
# # Excersize 3: Leap Year
# year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#             if year % 400 == 0:
#                 print("Leap year.")
#             else:
#                 print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adukt tickets are $12.")
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3
    print(f"Your finall bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Excersize 3 Pizza Order
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
else:
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")

# Excersie 4 Love counter
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
complete_name = lower_case_name1 + lower_case_name2
t = complete_name.count("t")
r = complete_name.count("r")
u = complete_name.count("u")
e = complete_name.count("e")
l = complete_name.count("l")
o = complete_name.count("o")
v = complete_name.count("v")
true = t + r + u + e
love = l + o + v + e
number = str(true) + str(love)
if int(number) < 10 or int(number) > 90:
    print(f"Your score is {number}, you go together like coke and mentos.")
elif 40 < int(number) < 50:
    print(f"Your score is {number}, you are alright together.")
else:
    print(f"Your score is {number}.")

# Play Game
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
answer_1 = input("left or right?")
if answer_1 == "right":
    print("Game Over.")
else:
    answer_2 = input("swim or wait?")
    if answer_2 == "swim":
        print("Game Over.")
    else:
        answer_3 = input("Which door?")
        if answer_3 == "red":
            print("Game Over.")
        elif answer_3 == "blue":
            print("Game Over.")
        else:
            print("You Win!")
