# DG8002 - F26 - Activity 3
# Author Name: Abdullah Alhomoud
# Date: 2026-09-26

# SCENARIO
# A group is splitting a restaurant bill, including a tip.
# For this exercise, use these starting values:
# Meal cost (before tip): $80.00
# Tip rate: 18% (store this as 0.18)
# Number of people: 4
# Ignore taxes for this simplified calculation.

# TODO 1: Create variables for the meal cost, tip rate, and number of people.
meal_cost_string = input("Enter the cost of the meal: $")
tip_percentage_string = input("Enter the percentage you would like to tip: ")
number_of_people_string = input("Enter the number of people in your party: ")

meal_cost = float(meal_cost_string)
tip_percentage = float(tip_percentage_string)
tip_rate = tip_percentage / 100
number_of_people = float(number_of_people_string)

# TODO 2: Calculate the dollar amount of the tip.
tip_amount = tip_rate * meal_cost

# TODO 3: Calculate the total bill, including the tip.
total_bill = meal_cost + tip_amount

# TODO 4: Use an if/else statement to check whether the number of people
# is greater than zero.
#   - If it is, calculate the cost per person and print the tip amount,
#     total bill, and cost per person.
#   - Otherwise, print a helpful message explaining why the bill
#     cannot be split.
if number_of_people > 0:
    cost_per_person = total_bill / number_of_people
    print("Tip amount is $" + f"{tip_amount:.2f}\nTotal bill: $" + f"{total_bill:.2f}\nCost per person: $" + f"{cost_per_person:.2f}")
else:
    print("The bill cannot be split, because there is no one in your party!")

# CHECK YOUR WORK
# With the starting values above:
# Tip: $14.40
# Total: $94.40
# Per person: $23.60
# Test again with zero people. Your program should not divide by zero.