print("Welcome to My Personal Mini-Toolkit!")

while True:
    print("\nPlease choose a tool:")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Checker")
    print("4. Quit")

    choice = input("Enter your choice: ")
    if choice == "1":
        # Simple Calculator: performs basic calculations with two numbers.
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        operation = input("Enter your operation: ")

        if operation == "1":
            result = num1 + num2
            print(f"The answer is {result}.")

        elif operation == "2":
              result = num1 - num2
              print(f"The answer is {result}.")

        elif operation == "3":
              result = num1 * num2
              print(f"The answer is {result}.")

        elif operation == "4":
            if num2 == 0:
                print("Sorry, you cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The answer is {result}.")

        else:
            print(f"Sorry, {operation} is not a valid operation.")
   
    elif choice == "2":
        # To-Do List: lets the user add, remove, and view tasks.
        tasks = []

        while True:
            print("\nTo-Do List")
            print("1. Add task")
            print("2. Remove task")
            print("3. Show tasks")
            print("4. Back to main menu")

            task_choice = input("Enter your choice: ")

            if task_choice == "1":
                task = input("Enter a task: ")
                tasks.append(task)
                print(f"Task '{task}' was added.")

            elif task_choice == "2":
                task = input("Enter the task to remove: ")

                if task in tasks:
                    tasks.remove(task)
                    print(f"Task '{task}' was removed.")
                else:
                    print(f"Sorry, '{task}' is not on your list.")

            elif task_choice == "3":
                if len(tasks) == 0:
                    print("Your to-do list is empty.")
                else:
                    print("\nYour tasks:")
                for task in tasks:
                    print(f"- {task}")

            elif task_choice == "4":
                print("Returning to the main menu.")
                break

            else:
                print(f"Sorry, {task_choice} is not a valid choice.")

    elif choice == "3":
        # Number Checker: checks whether a number is even or odd and its sign.
        number = int(input("Enter a number: "))

        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")

        if number > 0:
           print(f"{number} is positive.")
        elif number < 0:
           print(f"{number} is negative.")
        else:
           print(f"{number} is zero.")

    elif choice == "4":
        print("Thanks for using My Personal Mini-Toolkit! Goodbye!")
        break

    else:
        print(f"Sorry, that is not a valid choice. Please choose a number from 1 to 4.")