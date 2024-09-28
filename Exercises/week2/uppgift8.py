class TodoList:
    def __init__(self):
        self.tasks = []

    # Lägger till en ny uppgift i todo-listan
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Uppgiften '{task}' har lagts till i listan.")


    # Markera en uppgift som slutförd
    def mark_task_completed(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                print(f"Uppgiften '{task}' har markerats som slutförd.")
                return
        print(f"Uppgiften '{task}' hittades inte i listan.")


    # Visa alla uppgifter (både slutförda och oavslutade)
    def show_all_tasks(self):
        if not self.tasks:
            print("Inga uppgifter i listan.")
        else:
            print("Alla uppgifter:")
            for t in self.tasks:
                status = "Slutförd" if t["completed"] else "Oavslutad"
                print(f"- {t['task']} ({status})")

    # Visa endast oavslutade uppgifter
    def show_unfinished_tasks(self):
        unfinished_tasks = []

        # om task inte slutförd 
        for t in self.tasks:
            if not t["completed"]:
                unfinished_tasks.append(t)

        if not unfinished_tasks:
            print("Alla uppgifter är slutförda!")
        else:
            print("Oavslutade uppgifter:")
            for t in unfinished_tasks:
                print(f"- {t['task']}")


def main():
    todo_list = TodoList()

    while True:
        print("\nVälj ett alternativ:")
        print("1. Lägg till en uppgift")
        print("2. Markera en uppgift som slutförd")
        print("3. Visa alla uppgifter")
        print("4. Visa endast oavslutade uppgifter")
        print("5. Avsluta")

        choice = input("Ditt val: ")

        if choice == '1':
            task = input("Ange uppgift: ")
            todo_list.add_task(task)

        elif choice == '2':
            task = input("Ange uppgift att markera som slutförd: ")
            todo_list.mark_task_completed(task)

        elif choice == '3':
            todo_list.show_all_tasks()

        elif choice == '4':
            todo_list.show_unfinished_tasks()

        elif choice == '5':
            print("Avslutar programmet.")
            break

        else:
            print("Ogiltigt val, försök igen.")


if __name__ == "__main__":
    main()





