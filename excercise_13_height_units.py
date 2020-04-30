# Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from
# the user, followed by a number of inches. Once these values are read, your program
# should compute and display the equivalent number of centimeters.

ft = float(input("Enter the your height to be converted: "))
inches = float(input("Enter the inches: "))

height = (ft * 12 + inches) * 2.54

print("Your height in cm : ", height)
