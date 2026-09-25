# DG8002 - F26 - Activity 3
# Author Name: Abdullah Alhomoud
# Date: 2026-09-25

# SCENARIO
# Calculate SIMPLE interest on an investment. This exercise does not use
# compound interest, powers, or square roots.
# Formula: interest = principal * rate * time
# Start with:
# Principal (starting investment): $1,000.00
# Annual interest rate: 5% (store this as 0.05)
# Time: 3 years

# TODO 1: Create variables for the principal, annual interest rate, and time.
principal_amount_string = input("Enter the principal amount: $")
annual_interest_rate_percentage_string = input("Enter the annual interest rate percentage: ")
number_of_years_string = input("Enter the number of years: ")

principal_amount = float(principal_amount_string)
annual_interest_rate_percentage = float(annual_interest_rate_percentage_string)
annual_interest_rate = annual_interest_rate_percentage / 100
number_of_years = int(number_of_years_string)

# TODO 2: Calculate the interest earned using the formula above.
interest_accumulated = principal_amount * annual_interest_rate * number_of_years

# TODO 3: Calculate the final investment value (principal + interest).
final_investment_value = principal_amount + interest_accumulated

# TODO 4: Print the starting investment, interest earned, and final value.
# Optional: Format money to two decimal places.
print("Starting investment: $" + f"{principal_amount:.2f}\nInterest earned: $" + f"{interest_accumulated:.2f}\nTotal value: $" + f"{final_investment_value:.2f}")

# CHECK YOUR WORK
# Interest earned: $150.00
# Final value: $1,150.00