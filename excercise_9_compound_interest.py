# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.

interest_rate_per_year = 0.04
time = float(input("Enter time: "))
amount_deposited = float(input("Enter the amount which has been deposited: "))
compound_interest = amount_deposited * (pow(1 + (interest_rate_per_year / 100), time))

print("compound_interest is : {:.2f}".format(compound_interest))
