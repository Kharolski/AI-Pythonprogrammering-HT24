

# generator som producerar Fibonacci-sekvensen upp till ett givet antal termer
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a             # Returnera det aktuella talet i sekvensen
        a, b = b, a + b     # Beräkna nästa tal
        count += 1


# - Använda generatorn genom att iterera över den med en for-loop eller genom att anropa next().
# - next() för att få ett tal i taget, men när du har nått det sista värdet i generatorn 
#       kommer nästa anrop av next() att ge en StopIteration-undantag

# Använd generatorn för att skriva ut Fibonacci-sekvensen
n_terms = 5    # Antal termer
fib_gen = fibonacci_generator(n_terms)

# ---------------------------------------------------------------
print(f"Fibonacci-sekvensen upp till {n_terms} termer:")
# iterera över den med en for-loop
for fib_number in fib_gen:
    print(fib_number)

# ---------------------------------------------------------------
# iterera över den med next()
fib_gen_next = fibonacci_generator(5)

# Hantera StopIteration med try-except
try:
    while True:
        # Hämta nästa värde från generatorn
        print(next(fib_gen_next))
except StopIteration:
    # När sekvensen tar slut, hantera StopIteration
    print("Fibonacci-sekvensen är slut!")

# ----------------------------------------------------------------





