# Prompt user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Validate input
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    # Outer loop using while for rows
    while row < size:
        # Inner loop using for for columns
        for col in range(size):
            print("*", end="")  # Print asterisk without newline
        print()  # Move to the next line after each row
        row += 1