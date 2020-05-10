# Create a program that determines how quickly an object is traveling when it hits the
# ground. The user will enter the height from which the object is dropped in meters (m).
# Because the object is dropped its initial speed is 0m/s. Assume that the acceleration
# due to gravity is 9.8m/s2. You can use the formula vf =
# final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.
import math
height = int(input("Enter height in meters: "))
initial_speed = 0

acceleration = 9.8

final_speed = math.sqrt(initial_speed * initial_speed + 2 * acceleration * height)

print("Final speed: ", final_speed)
