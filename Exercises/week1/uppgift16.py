# Skriv ett python program som itererar mellan 1 och 50,

# om talet är delbart med 3 printar den "fizz"
# om talet är delbart med 5 printar den "buzz",
# om talet är delbart med både 3 och 5 så printar den "FizzBuzz"
# annars printar den bara ut talet


for number in range(1, 51):
    # Check if the number is divisible by both 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    # Check if the number is divisible by 3
    elif number % 3 == 0:
        print("Fizz")

    # Check if the number is divisible by 5
    elif number % 5 == 0:
        print("Buzz")
        
    # If the number is not divisible by 3 or 5, print the number itself
    else:
        print(number)
