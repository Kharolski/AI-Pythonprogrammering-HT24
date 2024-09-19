# Skriv ett program som genererar en enkel multiplikationsmodell för tal 1-10. 
# Hur snyggt kan du få tabellen? Läs på om sträng-formattering i Python.

def multiplication_table():

    # header row (top row)
    print("    ", end="")  # 4 spaces for alignment

    for i in range(1, 11):
        print(f"{i:4}", end="")  # Each number is right-aligned with 4 spaces
    print("\n" + "-" * 45)  # Divider line
    
    # multiplication rows
    for i in range(1, 11):

        # First column is the row number
        print(f"{i:2} |", end="")  # Row numbers right-aligned with 2 spaces

        for j in range(1, 11):
            print(f"{i * j:4}", end="")  # Multiply and right-align each result
        print()  # Move to the next line after each row

# print the table
multiplication_table()
