# DG8002 - F26 - Activity 3
# Author Name: Abdullah Alhomoud 
# Date: 2026-09-25

# SCENARIO
# You are converting Canadian dollars (CAD) into US dollars (USD).
# Use this exchange rate: 1 CAD = 0.72 USD.
# Start by converting 100 CAD. You may change the CAD amount to test your code.

# TODO 1: Create a variable for the amount in CAD and assign it the value 100.
cad_string = input("Enter the amount in Canadian dollars that you wish to convert: ")
cad = float(cad_string)

# TODO 2: Create a variable for the exchange rate and assign it the value 0.72.
exchange_rate = 0.72

# TODO 3: Calculate the amount in USD and store it in a new variable.
usd = cad * exchange_rate

# TODO 4: Print a clear message showing the CAD amount and the USD result.
print("CAD" + f"{cad:.2f}" + " is equal to USD" + f"{usd:.2f}")

# CHECK YOUR WORK
# 100 CAD should convert to 72 USD.