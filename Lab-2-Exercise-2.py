#Arjun N. Jalotjot
#BSCPE 1-3
#DSA

while True:
    try:
        # Step 1: Input the size of the array
        size = int(input("Enter the size of the array: "))
        if size <= 0:
            raise ValueError("Size must be a positive integer.")

        # Step 2: Input the elements of the array
        elements = input("Enter the elements separated by space: ").split()

        # Ensure the correct number of elements is provided
        if len(elements) != size:
            raise ValueError(f"You must enter exactly {size} elements.")

        # Convert input strings to integers
        elements = [int(num) for num in elements]

        # Step 3: Display the cube of each element
        for element in elements:
            print(element ** 3)

        break  # Exit the loop if everything is correct

    except ValueError as e:
        print(f"Error: {e}. Please try again.")
