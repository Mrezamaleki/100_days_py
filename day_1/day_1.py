
# **kw (name is not important by the way) == keywords such as dictionary
# *args == multiple values
def all_aboard(a, *args, **kw):
    print(a, args, kw)

#---------------------------------------------#

all_aboard(4, 7, 3, 0, x = 10, y = 64, z = 56)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [num +3 for num in numbers if num %2 == 0]

print(result)

# ---------------------------------------------#

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

print("Hello world!\nHello world!\nHello world!")

print("Hello " + "Angela")
print("Hello" + " Angela")
print("Hello" + " " + "Angela")

print("Hello " + input("what is your name?"))

print( len( input("what is your name?") ) )

name = input("what is your name?")

print(name)

print( len(name) )

# ---------------------------------------------#


a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a:", a,"b:", b)

# ---------------------------------------------#


print("Welcome to the Band Name Generator.")
City = input("What's the name of the city you grew up in?\n")
Pet = input("What's your pet's name?\n")
print("Your band name could be "+ City + " " + Pet)
