# Write a program that reads a positive integer, n, from the user and then displays the
# sum of all of the integers from 1 to n. The sum of the first n positive integers can be
# computed using the formula:
# sum = (n)(n + 1) / 2

n = int(input("Enter a positive Integer: "))

sum = (n * (n + 1)) / 2

print("Sum of first n positive Integers is: ", sum)
