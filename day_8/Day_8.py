# def greet():
#     print("Hello Angela")
#     print("How do you do Jack Bauer?")
#     print("Isn't the weather nice today?")
#
# greet()
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you {name}")
#
# greet_with_name("Billie")
#
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
#
# greet_with("Jack Bauer", "Nowhere")
#
# def greet_with_disorder(name, location):
#     print(f"Hello {name}")
#     print(f"How do you {location}")
#
# greet_with_disorder(location = "Nowhere", name = "Jack Bauer")
#
#
# #Exercise 1
# def paint_calc(height, width, cover):
#     paint = int(np.ceil((height * width)/cover))
#     print(f"You'll need {paint} cans of paint.")
# import numpy as np
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)
#
# #Exercise 2
# import math
#
# def prime_checker(number):
#     prime = True
#     for i in range(2, number - 1):
#         if number % i == 0:
#             prime = False
#     if prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
#
# n = int(input("Check this number: "))
# prime_checker(number=n)

#Project
from logo import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(input, shift):
#     output = ""
#     for letter in input:
#        ind = alphabet.index(letter) + shift
#        if ind > 25:
#            ind = ind - 26
#
#        output += alphabet[ind]
#
#     return output
#
# def decrypt(input, shift):
#     output = ""
#     for letter in input:
#        ind = alphabet.index(letter) - shift
#        if ind < 0:
#            ind = ind + 26
#
#        output += alphabet[ind]
#
#     return output

def encrypt_decrypt(input, shift, direction):
    output = ""
    for letter in input:
        if letter in alphabet:
            if direction == "encode":
                ind = alphabet.index(letter) + shift
                if ind > 25:
                    ind = ind - 26
            elif direction == "decode":
                ind = alphabet.index(letter) - shift
                if ind < 0:
                    ind = ind + 26

            output += alphabet[ind]
        else:
            output += letter
    return output

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    out_put = encrypt_decrypt(input = text, shift = shift, direction = direction)
    print(f"Here's the {direction} resul: {out_put}")
    yes_or_no = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if yes_or_no == "no":
        should_continue = False
        print("Goodbye")
