# Skriv en funktion som beräknar fakulteten av ett givet tal
# Matte 5

def factorial(n):
    # Check if the number is 0 or 1 because their factorial is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Calculate the factorial by multiplying the number by each smaller number
        result = 1

        for i in range(2, n + 1):
            result *= i
        return result

# Get input from the user
number = int(input("Enter a number to calculate its factorial: "))

# Calculate the factorial
print(f"The factorial of {number} is {factorial(number)}")
