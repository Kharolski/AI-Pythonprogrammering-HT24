# Uppgift 7: Implementera en stack med en klass
# Skapa en klass Stack som implementerar en stack (sista in, första ut) datastruktur med metoderna:

# push(item): Lägger till ett element överst i stacken.
# pop(): Tar bort och returnerar det översta elementet i stacken.
# peek(): Returnerar det översta elementet utan att ta bort det.
# is_empty(): Returnerar True om stacken är tom, annars False.

class Stack():

    def __init__(self):
        self.stacklist = []
        self.length = 0

    def __str__(self):
        return str(self.stacklist)

    def push(self, item):
        self.stacklist.append(item)
        self.length += 1

    def pop(self):
        self.length -= 1
        return self.length.pop()

    def peek(self):
        return self.stacklist[-1]

    def is_empty(self):
        return len(self.stacklist) == 0


my_stack = Stack()

my_stack.push(2)

print(my_stack.peek())

