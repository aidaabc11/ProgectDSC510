# -----------------------------------------------
# DSC510 – Week 3 Programming Assignment
# Name: Marzieh Abbasi
# Description: This program asks the user for the company name
# and how many feet of cable they want to install.
# Then it calculates the total cost based on how many feet they ask for.
# -----------------------------------------------

# Print welcome message
print("Welcome to the Fiber Installation Program!")

# Retrieve the company name from the user
company_name = input("Please enter your company name: ")

try:
    # Retrieve the number of feet of fiber optic cable to be installed from the user
    feet = float(input("Enter the number of feet of fiber optic cable you need: "))

    # Check if the entered feet is a valid positive number
    if feet <= 0:
        print("Error: Please enter a positive number of feet for installation.")
    else:
        # Evaluate the total cost based upon the number of feet requested
        # Use if/elif/else for bulk discounts
        if feet > 500:
            price_per_foot = 0.55
        elif feet > 250:
            price_per_foot = 0.75
        elif feet > 100:
            price_per_foot = 0.85
        else:
            price_per_foot = 0.95

        # Calculate the total expense
        total_cost = feet * price_per_foot

        # Print a receipt for the user in a legible format
        print("\n--- Installation Receipt ---")
        print(f"Company Name: {company_name}")
        print(f"Feet to install: {feet:.2f} feet") # Display feet with 2 decimal places if it's float
        print(f"Price per foot: ${price_per_foot:.2f}") # Format price to two decimal places for currency
        print(f"Total cost: ${total_cost:.2f}") # Format total cost to two decimal places for currency
        print("----------------------------")

except ValueError:
    # Catch any ValueError exceptions if user input is not a valid number
    print("Invalid input: Please enter a numeric value for the number of feet.")