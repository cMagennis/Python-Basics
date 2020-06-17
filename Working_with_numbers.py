
# Starting off real easy here, I can print off numbers in Python as simple as this:

print(2)
print(4.3145)
print(-6.156)

# Basic numerical operations work much the same as other coding languages
print("-----------------\n")

print(2 + 4)
print(4 / 2)
print(2 * 4)
print(2 - 4)

print(2.2 + 4.65)
print(2 + 4)

print(3 * 5 + 6)
print(3 * (5 + 6))

print("-----------------\n")

# Slightly more complex, we can use the modular operation
# The following statement is read, 10 mod 3
# This will print out the remainder, so in this case 10 / 3 is 3, with a remainder of 1. 1 is printed.

print(10 % 3)

# ------------------
# Variable use

print("-----------------\n")
my_num = 5

print(my_num)

# We can convert a number to a string if we want to print out numbers alongside strings

print(str(my_num) + " is an excellent number.")

# Using the function abs will give us the absolute value, so in this case 6
my_num = -6
print(abs(my_num))

# Another useful function is pow, which will give us a number to the power of x
print(pow(3, 2))
print(pow(4, 6))

# This is the max function, which will pass us the highest number
print(max(4, 6))
# While min will do the opposite
print(min(4, 6))

# The round function will round a decimal up for down, important point is that a .5 will round down in this case
print(round(4.5))
print(round(4.6))

# --------------------------------
# --------------------------------
# --------------------------------

# Some more functions follow. However in order to get access we have to import the Math Module
# I'm assuming these functions are not kept on the "base" build in order to save space? Not sure yet.
# Anyway here's what it looks like

print("-----------------\n")

from math import *

# This will chop off the .7 as it is rounding our number down regardless of it's value
print(floor(3.7))
# Whereas this will do the opposite, rounding it up
print(ceil(3.7))

# Here we have the square root function
print(sqrt(36))



