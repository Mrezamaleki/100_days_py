# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
# print(format_name(input("What is your first name? "), input("what is your last name? ")))
#
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1]
#
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# Calculator
def add(n_1, n_2):
    return n_1 + n_2

def subtract(n_1, n_2):
    return n_1 - n_2

def multiply(n_1, n_2):
    return n_1 * n_2

def divide(n_1, n_2):
    return n_1 / n_2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


num_1 = float(input("What's the first number? "))

should_continue = True

for key in operations:
    print(key)

while should_continue:
    operation_sym = input("Pick an operation: ")
    num_2 = float(input("What's the next number? "))
    cal = operations[operation_sym]
    answer = cal(num_1, num_2)
    print(f"{num_1} {operation_sym} {num_2} = {answer}")
    if input(f"Type 'yes' to continue calculating with {answer}") == "y":
        num_1 = answer
    else:
        should_continue = False
