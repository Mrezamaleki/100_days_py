programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

#Retrieving items from dictionary.
# print(programming_dictionary["Function"])
#
# # Adding new items to dictionary.
# programming_dictionary["Loop"] = "The action of doing something over and over again."
#
# print(programming_dictionary)
#
# # Create an empty dictionary.
# empty_dictionary = {}
#
# # wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)
#
# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in ypur computer."
#
# print(programming_dictionary)
#
# # Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
#
# # Exercise 1
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
#
# for key in student_scores:
#     if student_scores[key] > 90:
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] > 80 and student_scores[key] < 91:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] > 70 and student_scores[key] < 81:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
# print(student_grades)
#
# #Nesting
# capitals = {
#   "France": "Paris",
#   "Germany": "Berlin",
# }
#
# #Nesting a List in a Dictionary
#
# travel_log = {
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }
#
# #Nesting Dictionary in a Dictionary
#
# travel_log = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }
#
# #Nesting Dictionaries in Lists
#
# travel_log = [
# {
#   "country": "France",
#   "cities_visited": ["Paris", "Lille", "Dijon"],
#   "total_visits": 12,
# },
# {
#   "country": "Germany",
#   "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#   "total_visits": 5,
# },
# ]
#
# # Exercise 2
#
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
#
# def add_new_country(country, number, cities):
#     new_country = {}
#     new_country["country"] = country
#     new_country["visits"] = number
#     new_country["cities"] = cities
#     travel_log.append(new_country)
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#
# print(travel_log)

from replit import clear

from art import logo
print(logo)

bid_dictionary = {}
finish = True

while finish:
    name = input("what is your name?")
    price = input("what is your bid? $")
    keep_going = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    bid_dictionary[name] = price
    if keep_going == "no":
        finish = False
    elif keep_going == 'yes':
        clear()

max = 0

for key in bid_dictionary:
    if int(bid_dictionary[key]) > max:
        max = int(bid_dictionary[key])
        winner = key

print(bid_dictionary)

print(f"The winner is {winner} with a bid of ${max}")