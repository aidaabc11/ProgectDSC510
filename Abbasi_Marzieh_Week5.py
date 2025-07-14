# DSC 510
# Week 6
# Programming Assignment Week 6
# Author: Marzieh Abbasi
# Date: 07/13/2025

# Description:
# This program allows the user to input temperatures and stores them in a list.
# It then determines and prints the number of temperatures, the highest, the lowest,
# and the average temperature.

def get_temperature_input():
    """
    Prompts the user to enter temperatures until 'done' is entered.
    Returns a list of valid temperatures.
    """
    temperatures = []

    print("Enter temperatures one by one. Type 'done' when finished.\n")

    while True:
        user_input = input("Enter a temperature (or 'done' to finish): ").strip().lower()
        if user_input == 'done':
            break
        try:
            temp = float(user_input)
            temperatures.append(temp)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done' to stop.")
        except Exception as e:
            # Catch any other unexpected errors during input
            print(f"An unexpected error occurred during input: {e}")

    return temperatures

def calculate_average_temperature(temperatures):
    """
    Calculates the average temperature from a list of temperatures.
    Returns the average as a float, or 0.0 if the list is empty to prevent division by zero.
    """
    if not temperatures:
        return 0.0
    return sum(temperatures) / len(temperatures)

def display_results(temperatures):
    """
    Displays the number of entries, highest, lowest, and average temperature.
    """
    if not temperatures:
        print("No temperatures were entered for analysis.")
        return

    try:
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        count = len(temperatures)
        average_temp = calculate_average_temperature(temperatures)

        print("\n--- Temperature Summary ---")
        print(f"Total temperatures entered: {count}")
        print(f"Highest temperature: {max_temp:.2f}°C")
        print(f"Lowest temperature: {min_temp:.2f}°C")
        print(f"Average temperature: {average_temp:.2f}°C")
    except Exception as e:
        # Catch any unexpected errors during calculation or display
        print(f"An error occurred while processing or displaying results: {e}")


def main():
    """
    Main function to orchestrate the temperature collection, analysis, and display.
    """
    # Program Header
    print("-----------------------------------------")
    print("****** Temperature Analysis Program *****")
    print("-----------------------------------------")

    # Get temperatures from the user
    temperatures = get_temperature_input()

    # Display the analysis results (including the new average calculation)
    display_results(temperatures)


# Program execution starts here
if __name__ == "__main__":
    main()

