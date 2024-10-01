def divide_numbers():
    try:
        num1 = int(input("Ange första talet: "))
        num2 = int(input("Ange andra talet: "))

        result = num1 / num2

    except ZeroDivisionError:
        # Hantera division med noll
        print("Fel: Du kan inte dividera med noll!")
    
    except ValueError:
        # Hantera fall där input inte är ett tal
        print("Fel: Du måste mata in giltiga heltal!")

    else:
        # skriv ut resultatet
        print(f"Resultat: {num1} / {num2} = {result}")

    finally:
        # körs oavsett om det inträffade ett fel eller inte
        print("Programmet är klart.")

divide_numbers()
