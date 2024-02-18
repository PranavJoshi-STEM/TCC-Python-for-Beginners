# ------ Chapter 4: Exercises ------
# Congratulations, you have finished today's lesson.  Now, try to complete
# These challenges:
"""
Radian to degrees calculator:
    For this program, pi = 3.141592653589,
(NOTE: WRITE THIS IN A WAY PYTHON WILL UNDERSTAND)
Formula: radians * (180 / pi) = degrees
"""

pi = 3.141592653589

# ask for radians
rad = float(input('What is your radian amount?: '))

# calculate degrees
deg = rad*(180/pi)

# print degrees
print('Your degree amount is: '+str(deg), end=' degrees')