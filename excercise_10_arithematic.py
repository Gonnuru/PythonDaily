# Create a program that reads two integers, a and b, from the user.
# Your program should compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of a^b

import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b
difference = a - b
product = a * b
quotient = a // b
remainder = a % b
logarithmic = math.log10(a)
power = a ** b

print("Sum of two numbers is: ", sum)
print("Difference of two numbers is: ", difference)
print("Product of two numbers is: ", product)
print("Quotient of two numbers is: ", quotient)
print("Remainder of two numbers is: ", remainder)
print("logarithm base 10 of a is: ", logarithmic)
print("a to the power b is: ", power)
