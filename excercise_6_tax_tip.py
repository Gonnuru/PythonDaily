# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places.

cost_of_meal = float(input("Enter the cost of meal: "))
tax = 0.20
tip = cost_of_meal * 0.18

grand_total = cost_of_meal + tax + tip

print("Cost of Meal : {:.2f}".format(cost_of_meal))
print("Tax amount: {:.2f}".format(tax))
print("Tip: {:.2f}".format(tip))

print("Total amount : {:.2f}".format(grand_total))
