# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.

length = float(input("Enter the length of field in feet: "))
width = float(input("Enter the width of field in feet: "))

area_in_feet = length * width
one_acre = 43560
area_in_acre = area_in_feet / one_acre

print("The are of the field is : " + str(area_in_acre) + " acres")
