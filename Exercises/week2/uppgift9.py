

# bass class
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    # Metod som kan överskridas i subklasser
    def make_sound(self):
        return f"{self.name} makes a sound: {self.sound}"
    

# Subklass Dog som ärver från Animal
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "woof")

    # Metod som kan överskridas i subklasser
    def make_sound(self):
        return f"{self.name} says: Woof!"
    
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "meow")

    # Metod återanva basklassens logik metod
    def make_sound(self):
        return super().make_sound()

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "moo")

    def make_sound(self):
        return f"{self.name} says: Moo!"

def animal_chorus(animals):
    for animal in animals:
        print(animal.make_sound())

def main():

    dog = Dog("Rover")
    cat = Cat("Whiskers")
    cow = Cow("Bessie")

    animals = [dog, cat, cow]

    print("Animal Chorus:")
    animal_chorus(animals)
    


if __name__ == "__main__":
    main()
