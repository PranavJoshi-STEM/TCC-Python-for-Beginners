# In this video, we'll cover:
'''
Basic syntax:
    - The types of comments
    - Indentation and newline vs curly brackets and semicolons

Functions and variables:
    - The print function
        - What are arguments, parameters and functions
    - The input function
    - Variable types
        - What are variables
        - Assignment
        - The type function
        - Tuple unpacking and packing

Operations:
    - Operations on numbers
    - Operations on variables
        - F-strings
    - Brackets
    - Logic gates

Exercises:
    - Implement the pythagoras thereom
    - Make a radian to degree calculator
'''






# ------ Chapter 1: Basic Syntax ------
#    - The types of comments
#    - Indentation and newline vs curly brackets and semicolons

# There are 2 ways to write comments in python,
# First method is like this: Comment out every after a hashtag
'''Second method is like this: Wrap all your code in triple quotes'''
"""
Note:
In Python, single quotes and double quotes all have the same purpose.  This
can be useful in certain situations like we'll see later in this video.
"""

# In python, we don't use curly brackets and semicolons
# For example, take a look at C++ (2_Example.cpp)
# Instead, we use new lines and indentation to write code:

def main():
    print('Hi')
    print('I think we should eat ice-cream today!')







# ------ Chapter 2: Functions and Variables ------
#    - The print function
#        - What are arguments, parameters and functions
#    - The input function
#    - Variable types
#        - What are variables
#        - Assignment
#        - The type function
#        - Tuple unpacking and packing


# Chapter 2, exercise 1
print() # <-- This is a *function*, use brackets to indicate so
print('Hello', 'world!') # <-- These are passed in to functions as *arguments*
print('Hello', 'world!', sep=' ', end='')
#                        ^^^^^^^^^^^^^^^ These are also arguments too, they
#                                        are optional though.


# Chapter 2, exercise 2
input() # <-- This gets input
name = input('Hi, what is your name?') # <-- This also gets input
print('Whoa, your name is', name) # <-- Lets check the result!


# Chapter 2, exercise 3
# Variables are things that hold data.  To assign a value, use the = operator
my_int = 12
my_float = 12.0
my_bool = True # bools can be True or False
my_list = ["I'm", 'a', 'list!']
my_str = 'Did you know that this morning, I screamed "AH"\
because I stubbed my toe D:' # immutable
my_dict = {"TCC's favourite food": "Pizza",
           'My favourite subject': 'Math!'}
print(my_dict["TCC's favourite food"]) # output: Pizza
my_set = {'Hi', "it's a nice day today!"} # notice how : isn't used here
# Tuples can be a combination of different types
my_tuple = ('Lots of different', ['different', 'types'], 12) # immutable

# The type() function takes in a variable and returns the type, this can be
# useful when debugging
print(type(my_set))
print(my_set)

# to unpack the tuple, you can do this
(a, b, c) = my_tuple
print(a, b, c)

# to convert types, simply put it in the function of your preferred type
print('12' == str(12)) # in general, if it makes sense, it works!






# ------ Chapter 3: Operations ------
#    - Operations on numbers
#    - Operations on variables
#        - F-strings
#    - Brackets
#    - Logic gates


# Python follows the rules of PEDMAS
# Parenthesis, exponents, division or multiplication (left to right),
# addition or subtraction (left to right)

# Operations on numbers
addition = 1 + 3 # note, spacing between operations doesn't matter!
subtraction = 1-3
multiplication = 1*3 # * is the multiplication sign
exponent = 1**3 # ** is exponent sign.  NOTE: ** and * * are not the same!

# There are 3 division operators
# Normal division
div = 15/4 # returns float
print(div) # output: 3.75

# Floor division
floor_div = 15//4 # the whole number of times b goes into a, returns int
print(floor_div) # output: 3
# ^^^^^^^^^^^^^^ Since 4*3=12 is the total number of times b can be multiplied
#                before it exceeds a, the answer is 3.

# Modulus
mod = 15%4 # the remainder of a divided by b
print(mod) # output: 3
# ^^^ Since 12 is the highest multiple of b under a, mod is the remainder (3)

# Shorthand operations:
# Many times, we need to write simple equations, here are some common
# shorthand equations
"""
a += b      ==>     a = a + b
a -= b      ==>     a = a - b
a //= b     ==>     a = a // b
a /= b      ==>     a = a / b
a %= b      ==>     a = a % b
a *= b      ==>     a = a * b
a **= b     ==>     a = a ** b
"""


# Operations on variables:
# Variables that are not type int or float can also be operated on, as long
# as all the variables are of the same type!

super_long_str = "Hi, I'm The Canadian Coder!" + 'My favourite movie is "Top Gun Maverick"!'
ultra_long_str = ('He'+'llo') + 'o'*12 # string multiplication is one of the rare exceptions
#                ^^^^^^^^^^^^ Using brackets to manipulate PEDMAS
super_long_list = ['Hi!'] + ['I like', 'pineapple on pizza!', 4]

# Python uses the same symbols for multiple things, the ** here means unpacking (NOT EXPONENTS)
dict_1 = {'food': 'pizza', 'health':15}
dict_2 = {'spells': 4, 'spell_type':'fire'}
combined_dict = {**dict_1, **dict_2}

# Exercise:
# In many cases, you will have to debug by printing variables.
health = 15
hunger = 0.95
name = 'Zelgorath'

# In these cases, use f-strings since they are easier to read.
# An f-string starts with an f before the string, and uses curly brackets
# to display variables.
print(f'Name: {name}, Hunger: {hunger}, Health: {health}')

# Now that you know how to use operations on variables,
# lets talk about logic gates.
"""
There are many logic gates, but here are the main ones you need to know:
a == b     ==> returns True if a is the same value as b
a != b     ==> returns True if a is NOT the same value as b
a < b      ==> straight-forward
a > b      ==> straight-forward
a <= b     ==> straight-forward, is b is greater than or equal to
a >= b     ==> straight-forward, if b is less than or equal to


not a      ==> a keyword that negates the value (changes True to False and vice-versa)
a or b     ==> Returns True if atleast 1 of a or b is True
a and b    ==> Returns True if a and b are True
"""





# ------ Chapter 4: Exercises ------
# Congratulations, you have finished today's lesson.  Now, try to complete
# These challenges:
"""
Pythagoras thereom calculator:
    Ask for a and b and return c.
(NOTE: WRITE THIS IN A WAY PYTHON WILL UNDERSTAND)
Formula: a**2 + b**2 = c**2


Radian to degrees calculator:
    For this program, pi = 3.141592653589,
(NOTE: WRITE THIS IN A WAY PYTHON WILL UNDERSTAND)
Formula: radians * (180 / pi) = degrees
"""