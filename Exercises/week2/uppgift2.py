# Skriv en klass Matte Den ska ha följande metoder

# add(a,b): Returnerar summan
# subtract(a,b): returnerar skillnaden
# divide(a,b): returnerar divisionen
# multiply(a,b): returnerar multiplikationen
# gcd(a,b): returnerar största gemensamma delare
# area_circle(r): returnerar arean av en cirkel
# circumference(d): returnerar omkretsen av en cirkel


class Matte():

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
    def divide(self, a, b):
        return a / b
    
    def multiply(self, a, b):
        return a * b
    
    def gcd(self, a , b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
    
    def area_circle(self, r):
        pi = 3.141592653589793
        if r < 0:
            return "Radien kan inte vara negativ"
        return pi * r ** 2  # Beräkna arean
    
    def circumference(self, d):
        pi = 3.141592653589793
        if d < 0:
            return "Radien kan inte vara negativ"
        return 2 * pi * d  # Beräkna omkretsen  

def main():
    matte = Matte()

    num1 = int(input("Ange första numret: "))
    num2 = int(input("Ange andra numret: "))
    result = matte.multiply(num1, num2)
    print(f"Multiplikation mellan {num1} och {num2} resultat är: {result}")

    num3 = int(input("Ange första numret: "))
    num4 = int(input("Ange andra numret: "))
    result1 = matte.gcd(num3, num4)
    print(f"Största gemensamma delare (GCD) mellan {num3} och {num4} är: {result1}")

    # Beräkna arean
    radius = float(input("Ange radien på cirkeln: "))
    area = matte.area_circle(radius)
    print(f"Arean av cirkeln med radien {radius} är: {area}")

    # Beräkna omkretsen
    circumference = matte.circumference(radius)
    print(f"Omkretsen av cirkeln med radien {radius} är: {circumference}")


if __name__ == "__main__":
    main()