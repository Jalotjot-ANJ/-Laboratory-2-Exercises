#Arjun N. Jalotjot
#BSCPE 1-3
#DSA

# Function to generate an inverted right triangle
def generate_inverted_triangle(n):
    for i in range(n, 0, -1):
        print('*' * i)

# Main part of the program
while True:
    try:
        # Input the height of the triangle
        height = int(input("Enter the height of the triangle: "))
        if height < 1:
            raise ValueError("Height must be at least 1.")
        
        # Generate and display the inverted triangle
        generate_inverted_triangle(height)
        break  # Exit the loop if input is valid

    except ValueError as e:
        print(f"Error: {e}. Please try again.")
