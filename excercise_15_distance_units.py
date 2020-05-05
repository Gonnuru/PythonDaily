# In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles.

distance_in_ft = float(input("Enter the distance in feet: "))

distance_in_inches = distance_in_ft * 12
distance_in_yards = distance_in_ft / 3
distance_in_miles = distance_in_ft / 5280

print("Distance in feet to inches: ", distance_in_inches)
print("Distance in feet to yards", distance_in_yards)
print("Distance in feet to miles: ", distance_in_miles)
