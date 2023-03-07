#Excercise 1
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
sum_height = 0
number_students = 0
for i in student_heights:
    sum_height += i
    number_students += 1
print(round(sum_height/number_students))

#Excercise 2
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
highest_score = 0
for i in student_scores:
    if i > highest_score:
        highest_score = i
print(f"The highest score in the class is: {highest_score}")

#Excercise 3
sum_even = 0
for i in range (1,51):
    sum_even += 2*i
print(sum_even)

#Exercise 4
for i in range (1,101):
    if i % 3 == 0:
        if i % 15 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i % 5 == 0:
        if i % 15 == 0:
            print("FizzBuzz")
        else:
            print("Buzz")
    else:
        print(i)

#Random Code Generation
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []
for i in range (0, nr_letters):
    password.append(letters[random.randint(0, len(letters) - 1)])
for i in range (0, nr_numbers):
    password.append(numbers[random.randint(0, 9)])
for i in range (0, nr_symbols):
    password.append(symbols[random.randint(0, 8)])
Py_Password_easy = ''
for i in password:
    Py_Password_easy += i
print(Py_Password_easy)
random.shuffle(password)
Py_Password_hard = ''
for i in password:
    Py_Password_hard += i
print(Py_Password_hard)