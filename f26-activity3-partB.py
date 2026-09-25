# DG8002 - F26 - Activity 3
# Author Name: Abdullah Alhomoud
# Date: 2026-09-25

# SCENARIO
# Convert a temperature from Celsius to Fahrenheit.
# Formula: Fahrenheit = (Celsius * 9 / 5) + 32
# Start with a temperature of 20 degrees Celsius.

# TODO 1: Create a variable for the Celsius temperature and assign it 20.
celcius_string = input("Enter the temperature in Celcius: ")
celcius = int(celcius_string)

# TODO 2: Use the formula above to calculate Fahrenheit.
# Store the result in a separate variable.
fahrenheit = celcius * 9 / 5 + 32

# TODO 3: Print a clear message showing both temperatures and their units.
print(celcius_string + "°C is equal to " + str(fahrenheit) + "°F.")

# CHECK YOUR WORK
# Input: 20 degrees Celsius
# Expected output: 68 degrees Fahrenheit