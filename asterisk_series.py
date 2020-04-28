# write a program that prints Pattern like this
#       input : 7
# * * * * * * *

num_range = int(input("Enter the range: "))
for i in range(1, num_range + 1):
    print("* ", end=" ")
