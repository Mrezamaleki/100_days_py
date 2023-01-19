# Data types

# String

print("Hello"[0]) #Subscript
print("123" + "345")

#Integer

print(123 + 345)

print(123_456_789) #like 123,456,789 = 123456789
#Float

print(3.14159)

Boolean = True , False

num_char = len(input("what is your name?"))
new_num_char = str(num_char)
print("Your name contains " + new_num_char + "characters")
#
a = float(123)
print(type(a))
print(70 + float("100.5"))
print(str(70) + str(100))

#Exercise 1
two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0]) + int(two_digit_number[1]))

#Excersise 2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
print(int(float(weight)/(float(height)**2)))

print(round(8/3, 2))
print(8 // 3)

score = 0
height = 1.8
isWining = True
#f-String
print(f"your score is {score}, your height is {height}, you are winning is {isWining}")

#Excersise 3
age = input("What is your current age? ")
remain_age = 90 - int(age)
months = 12 * remain_age
weeks = 52 * remain_age
days = 365 * remain_age
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# Tip Calculator

print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
pay = round(float(total_bill) * (1+(int(tip)/100))/int(people),2)
print(f"Each person should pay: ${pay}")