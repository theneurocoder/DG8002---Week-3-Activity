# DG8002 - F26 - Activity 3
# Author Name: Abdullah Alhomoud
# Date: 2026-09-25

# SCENARIO
# A group of friends is planning a road trip and wants to estimate the
# driving time and fuel cost. Use these starting values:
# Distance: 650 km
# Average speed: 100 km/h
# Fuel efficiency: 8 L per 100 km
# Fuel price: $1.55 per litre
# Passengers: 3
# Assume constant average speed and fuel efficiency. Ignore stops,
# traffic, taxes, and other vehicle costs.

# TODO 1: Create five variables to store the trip information above.
# Give each variable a meaningful name.
distance_string = input("Enter the distance in km: ")
average_speed_string = input("Enter the average speed in km/hr: ")
fuel_efficiency_string = input("Enter the fuel efficiency in litres/100km: ")
fuel_price_string = input("Enter the fuel price in $/litre: ")
number_of_passengers_string = input("Enter the number of passengers: ")

distance = float(distance_string)
average_speed = float(average_speed_string)
fuel_efficiency = float(fuel_efficiency_string)
fuel_price = float(fuel_price_string)
number_of_passengers = int(number_of_passengers_string)

# TODO 2: Calculate estimated driving time in HOURS.
# Hint: distance / average speed
estimated_driving_time = distance / average_speed

# TODO 3: Calculate the total fuel needed in LITRES.
# Hint: fuel efficiency describes litres used for every 100 km.
fuel_needed = distance * fuel_efficiency / 100

# TODO 4: Calculate the total fuel cost.
total_fuel_cost = fuel_needed * fuel_price

# TODO 5: Use an if/else statement to check that passengers is greater
# than zero before calculating the fuel cost per passenger.
# If passengers is zero or less, print a helpful message instead.
if number_of_passengers <=0:
    print("You need at least one passenger to calculate the fuel cost per passenger.")

# TODO 6: Print a readable trip summary showing:
#   - Estimated driving time (hours)
#   - Total fuel needed (litres)
#   - Total fuel cost (CAD)
#   - Fuel cost per passenger (CAD), when it can be calculated
else:
    fuel_cost_per_passenger = total_fuel_cost / number_of_passengers
    print("Estimated driving time: " + str(estimated_driving_time) + " hours\nTotal fuel needed: " + str(fuel_needed) + " litres\nTotal fuel cost: CAD" + f"{total_fuel_cost:.2f}" + "\nFuel cost per passenger: CAD" + f"{fuel_cost_per_passenger:.2f}")

# CHECK YOUR WORK
# With the starting values above, expect:
# Driving time: 6.5 hours
# Fuel needed: 52 litres
# Total fuel cost: $80.60
# Fuel cost per passenger: about $26.87
# Test again with zero passengers. Your program should not divide by zero.