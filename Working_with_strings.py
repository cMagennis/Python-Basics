"""
First instance of adding a new line by using \n
The \ is known, in this context, as the escape character.
It allows the program to take whatever character follows literally

As an aside, I am using a multiline string to comment as Python ignores strings not assigned to a variable
Usually # is used for single line comments
"""

print("Giraffe\nAcademy")

phrase = "Giraffe Academy"
print(phrase + ". This process is called concatenation. " + "It is where we attach two or " +
                                                            "more strings together.")


# Here's a couple common functions:
# Starting with .lower() to change it to lowercase
phrase = ("\n" + phrase.lower())
print(phrase)

# Changing it back to test our function
phrase = "\nGIRaffE ACademy\n"
print(phrase)

# Or to tidy it up a bit:
print(phrase.lower() + "\n")

# Similarly we have .upper()
# Causing the opposite effect
print(phrase.upper())

# In order to actually change the variable, we would need to assign it like so:
phrase = (phrase.lower())

# We can also check if the whole string is in upper or lower case using isupper() or islower()
# This will return a Boolean result, so True or False
print(phrase.isupper())
print(phrase.islower())

# Functions can be chained together, a good way to have neater code:
print(phrase.upper().isupper())

# -------------
# Another function, length = .len
# Interestingly, the /n from earlier does add a character as I was getting 17 from the phrase variable instead of 15
phrase = "Giraffe Academy"
print(len(phrase))


# -------------
# Index, using square brackets [] we can select a certain character in a string
print(phrase [0])

# There's a function that we can use to get a certain index
# This function will return an index depending on the parameter I give to it
# This one is returning the first a in the string only, so 3
print(phrase.index("a"))

# The case matters too, this will return 0
print(phrase.index("G"))

# Whereas this will not work
# print(phrase.index("g"))

# You can use words as a parameter too
# This returns 8, as that is where the word starts
print(phrase.index("Academy"))

# ---------------
# Replace function, the parameter you want to replace goes first and the desired replacement goes after the ,

print(phrase.replace("Giraffe", "Elephant"))

