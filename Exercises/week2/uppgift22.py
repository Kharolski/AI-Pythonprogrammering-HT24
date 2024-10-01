# Uppgift 22: Intro decorators

# --------------------------------------------------------------------
# Uppgift 22:

import time

def timer(func):
    def wrapper(*args, **kwargs):
        
        start_time = time.time()        # Starta tidtagningen innan funktionen körs
        result = func(*args, **kwargs)  # Kör själva funktionen
        end_time = time.time()          # Stoppa tidtagningen efter funktionen körts
        execution_time = end_time - start_time  # Beräkna exekveringstiden
        
        print(f"{func.__name__} kördes på {execution_time:.4f} sekunder.")
        return result
    return wrapper

@timer
def quick_function():
    print("Denna funktion körs snabbt!")
    time.sleep(1)   # Pausa i 1 sekund

@timer
def slow_function():
    print("Denna funktion tar lite längre tid!")
    time.sleep(3)  # Pausa i 3 sekunder


quick_function()
slow_function()


# --------------------------------------------------------------------
# Intro:

def my_decorator(func):
    def wrapper():
        print("först körs innan funktionen!")
        func()
        print("Andra körning efter funktionen!")
    
    return wrapper


@my_decorator
def say_hallo():
    print("Hello! från funktionen.....")

# samma sak som: ------
# def say_hello():
#     print("Hello!")

# say_hello = my_decorator(say_hello)
























