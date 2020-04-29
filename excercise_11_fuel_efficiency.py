# In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon
# (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
# kilometers (L/100 km). Use your research skills to determine how to convert from
# MPGto L/100 km. Then create a program that reads a value from the user in American
# units and displays the equivalent fuel efficiency in Canadian units.

miles_per_gallon = float(input("Enter the number of miles per gallon to be converted: "))

liters_100_km = 235.214583 / miles_per_gallon

print("The converted value is as follows : ",liters_100_km, "Liters per 100 Km")
