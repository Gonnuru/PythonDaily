# The volume of a cylinder can be computed by multiplying the area of its circular
# base by its height. Write a program that reads the radius of the cylinder, along with
# its height, from the user and computes its volume.

from math import pi
radius = float(input("Enter radius of cylinder: "))
height = float(input("Enter height of cylinder: "))

volume = pi * radius ** 2 * height

print("Volume of cylinder: {:.2f}".format(volume))
