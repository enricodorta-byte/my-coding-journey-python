# Exercise: While loop with user input
# Accumulate numbers until 0 is entered, then compute sum and average
# Date: 11 January 2026

total_sum = 0.0            # Use float to handle decimal averages
count = 0                  # Track number of valid inputs

print("Enter numbers (enter 0 to finish):")

while True:
    user_input = input("Number: ")

    try:
        number = float(user_input)  # Convert input to float
    except ValueError:
        print("Invalid input - please enter a number: ")
        continue

    if number == 0:
        break                       # Exit loop on 0 input

    total_sum += number
    count += 1           # Increment count of valid inputs

    # Output results
    if count > 0:
        average = total_sum / count
        print(f"\nResults:")
        print(f"Total sum: {total_sum}")
        print(f"Count of numbers: {count}")
        print(f"Average: {average: .2f}")
    else:
        print("\nNo numbers were entered.")