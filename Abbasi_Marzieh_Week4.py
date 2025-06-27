# -----------------------------------------------
# DSC510 – Week 4 Programming Assignment
# Name: Marzieh Abbasi
# Description: This program calculates the cost of fiber optic cable installation
# using functions. It asks the user for the company name and the length of cable,
# applies bulk discounts based on length, and prints a receipt.
# -----------------------------------------------

# Define a function to calculate cost based on feet and price per foot
def calculate_cost(feet, price_per_foot):
    return feet * price_per_foot

# Define the main function to control the flow of the program
def main():
    print("Welcome to the Fiber Installation Program!")
    
    company_name = input("Please enter your company name: ")
    
    try:
        feet = float(input("Enter the number of feet of fiber optic cable you need: "))
        
        if feet <= 0:
            print("Error: Please enter a positive number for feet.")
            return

        # Determine the price per foot using if/elif
        if feet > 500:
            price_per_foot = 0.55
        elif feet > 250:
            price_per_foot = 0.75
        elif feet > 100:
            price_per_foot = 0.85
        else:
            price_per_foot = 0.95
        
        # Call the function to calculate the total cost
        total_cost = calculate_cost(feet, price_per_foot)

        # Print a formatted receipt
        print("\n--- Installation Receipt ---")
        print(f"Company Name     : {company_name}")
        print(f"Feet to Install  : {feet:.2f}")
        print(f"Price per Foot   : ${price_per_foot:.2f}")
        print(f"Total Cost       : ${total_cost:.2f}")
        print("----------------------------")
    
    except ValueError:
        print("Invalid input: Please enter a numeric value for feet.")

# This ensures that main() only runs when the file is executed directly
if __name__ == "__main__":
    main()
