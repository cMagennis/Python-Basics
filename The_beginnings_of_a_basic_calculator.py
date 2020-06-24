# The following code will result in an incorrect result as if we gave it for example 2 and 2, it would return 22
# This is because when we get input from a user Python will, by default, convert the input to a string

num1 = input("Enter a number: ")

num2 = input("Enter another number: ")

result = num1 + num2

print("\nThe incorrect result is: \n")
print(result)

# So the fix is to convert the input from string to a number
# One way we can do that is with the int(integer) function as shown:

converted_num1 = int(num1)

converted_num2 = int(num2)

# We can tidy this up like this:

result = int(num1) + int(num2)

print("\nThe correct result is: \n")
print(result)

# However the int function cannot contain a decimal, as an integer is a whole number
# We can use the float function instead to include decimals

dec_num1 = input("Enter a decimal number: ")

dec_num2 = input("Enter another decimal number: ")

dec_result = float(dec_num1) + float(dec_num2)

# As I wanted to print the full result and string in one line, I had to use the str function to convert my result back
# from a float to a string:

print("\nThe correct decimal result is: \n" + str(dec_result))