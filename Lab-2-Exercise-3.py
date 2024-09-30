#Arjun N. Jalotjot
#BSCPE 1-3
#DSA

# Function to generate a hollow square
def generate_hollow_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:  # First and last row
            print('x' * n)
        else:  # Middle rows
            print('x' + ' ' * (n - 2) + 'x')

# Main part of the program
while True:
    try:
        # Input the side length of the square
        side_length = int(input("Enter the side length of the square: "))
        if side_length < 2:
            raise ValueError("Side length must be at least 2.")
        
        # Generate and display the hollow square
        generate_hollow_square(side_length)
        break  # Exit the loop if input is valid

    except ValueError as e:
        print(f"Error: {e}. Please try again.")
