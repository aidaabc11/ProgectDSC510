# DSC 510
# Week 2
# Programming Assignment Week 2
# Author: Marzieh Abbasi
# Date: 06/15/2025

# Change Control Log:
# Change#: 1
# Change(s) Made: Initial version created and tested.
# Date of Change: 06/15/2025
# Author: Marzieh Abbasi
# Change Approved by: Marzieh Abbasi
# Date Moved to Production: 06/15/2025
# -----------------------------------------------------
# This script calculates the total cost for installing fiber optic cable.
# The user provides the company name and the required length of cable in feet.
# It uses a fixed rate of $0.95 per foot and then prints a simple receipt with transaction details.
# -----------------------------------------------------

# Display a greeting message for the user
print("estimate the cost of your fiber optic cable installation.")

# Prompt the user to enter their company name
company_name = input("What is your company name? ")

# Ask for the length of cable needed in feet and convert the input to a float
# A try-except block could be added here for robust error handling,
# but for this assignment, direct conversion is sufficient.
feet_required = float(input("How many feet of fiber optic cable do you need to install? "))

# Define the fixed cost rate per foot
rate_per_foot = 0.95

# Calculate the total installation cost
installation_total = feet_required * rate_per_foot

# Display a formatted receipt showing the details of the transaction
print("\n========== Fiber Optic Installation Receipt ==========")
print(f"Company Name         : {company_name}")
print("------------------------------------------------------")
print(f"Cable Length Needed  : {feet_required} feet")
print(f"Price per Foot       : ${rate_per_foot:.2f}")
# Formatted to two decimal places for currency
print("------------------------------------------------------")
print(f"Total Cost Estimate  : ${installation_total:.2f}")
# Formatted to two decimal places for currency
print("======================================================")