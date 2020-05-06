# Write a program that begins by reading a radius, r , from the user. The program will
# continue by computing and displaying the area of a circle with radius r and the
# volume of a sphere with radius r .

from math import pi

radius = float(input("Enter the radius of circle: "))

area_of_circle = pi * radius ** 2

volume_of_sphere = 1.33 * pi * radius ** 3

print("Area of circle: ", area_of_circle)
print("Voulme of Sphere: ", volume_of_sphere)
