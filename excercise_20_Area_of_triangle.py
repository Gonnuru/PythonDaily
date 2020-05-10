# area of triangle when sides are known
import math
length_1 = int(input("Enter length of one side of a triangle: "))
length_2 = int(input("Enter length of side 2 of a triangle: "))
length_3 = int(input("Enter length of side 3 of a triangle: "))

side = (length_1 + length_2 + length_3) / 2

area = math.sqrt(side * (side - length_1) * (side * length_2) * (side * length_3))

print("Area of triangle: ", area)
