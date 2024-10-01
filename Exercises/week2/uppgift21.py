
class FibonacciIterator:
    def __init__(self, max_value):
        self.max_value = max_value  # Stoppa vid maxvärdet
        self.current = 0            # Det första talet i sekvensen
        self.next_value = 1         # Det andra talet i sekvensen

    def __iter__(self):
        return self                 # Returnera iteratorn själv
    
    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration     # Stoppa när vi når maxvärdet
        
        # Beräkna nästa Fibonacci-tal
        result = self.current

        self.current, self.next_value = self.next_value, self.current + self.next_value
        return result


# -----------------------------------------------------------------------------

# Enkelt Iterator list 

class SimpleListIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        # Kontrollera om det finns fler element
        if self.index < len(self.data):
            # Hämta nästa element
            element = self.data[self.index]
            # Flytta indexet till nästa position
            self.index += 1
            # Returnera elementet
            return element
        else:
            # Stoppa iterationen om listan är slut
            raise StopIteration


def main():
    # Generera Fibonacci-tal upp till 50
    max_fib_value = 50
    fib_iterator = FibonacciIterator(max_fib_value)

    print("Fibonacci-sekvens upp till", max_fib_value, ":")
    for number in fib_iterator:
        print(number)


    my_list = [10, 20, 30, 40, 50]
    iterator = SimpleListIterator(my_list)

    # Vi kan nu iterera över objektet med en for-loop
    print("My list:")
    for element in iterator:
        print(element)



if __name__ == "__main__":
    main()


