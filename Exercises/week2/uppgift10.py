# Vi kan använda abstrakta metoder för att tvinga subklasserna att implementera metoder.
# Som (area och perimeter) med ABC bibliotek
# from abc import ABC, abstractmethod
# och använda på vara abstrakt methoder @abstractmethod 


import math

# basklass för geometriska former
class GeometricShape:
    def __init__(self, name) -> None:
        self.name = name

    def area(self):
        # Abstrakt metod för att beräkna area
        raise NotImplementedError("Denna metod måste implementeras av en subklass")
    
    def perimeter(self):
        # Abstrakt metod för att beräkna omkrets
        raise NotImplementedError("Denna metod måste implementeras av en subklass")

    def __str__(self) -> str:
        # Returnerar en beskrivning av formen
        return f"{self.name} med area {self.area():.2f} och omkrets {self.perimeter():.2f}"


# Subklass för rektanglar
class Rectangle(GeometricShape):
    def __init__(self, width, height) -> None:
        super().__init__("Rektangel")
        self.width = width
        self.height = height

    def area(self):
        # Area = bredd * höjd
        return self.width * self.height
    
    def perimeter(self):
        # Omkrets = 2 * (bredd + höjd)
        return 2 * (self.width + self.height)
    
    def __str__(self) -> str:
        return f"{self.name}: bredd {self.width}, höjd {self.height}, area {self.area():.2f}, omkrets {self.perimeter():.2f}"


# Subklass för cirklar
class Circle(GeometricShape):
    def __init__(self, radius):
        super().__init__("Cirkel")
        self.radius = radius

    def area(self):
        # Area = pi * radie^2
        return math.pi * self.radius
    
    def perimeter(self):
        # Omkrets = 2 * pi * radie
        return 2 * math.pi * self.radius
    
    def __str__(self) -> str:
        return f"{self.name}: radie {self.radius}, area {self.area():.2f}, omkrets {self.perimeter():.2f}"


def main():
    # Skapar en rektangel med bredd 5 och höjd 10
    rectangle = Rectangle(5, 10)
    print(rectangle)

    # Skapar en cirkel med radie 7
    circle = Circle(7)
    print(circle)



if __name__ == "__main__":
    main()