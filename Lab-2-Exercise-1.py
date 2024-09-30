#Arjun N. Jalotjot
#BSCPE 1-3
#DSA

def power(base, exponent):
    # Base case: any number to the power of 0 is 1
    if exponent == 0:
        return 1
    # Recursive case: multiply the base by the power of (base, exponent-1)
    return base * power(base, exponent - 1)

# Main part of the program
while True:
    try:
        # Input the base and exponent
        base = int(input("Enter the base (a number): "))
        exponent = int(input("Enter the exponent (a non-negative integer): "))
        
        if exponent < 0:
            raise ValueError("Exponent must be a non-negative integer.")
        
        # Calculate and display the result
        result = power(base, exponent)
        print(f"{base}^{exponent} = {result}")
        break  # Exit the loop if input is valid

    except ValueError as e:
        print(f"Error: {e}. Please try again.")
