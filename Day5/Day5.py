todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos): # The enumerate returns a tuple  containing a tuple as in (index, item)
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            number = int(input("number of todo to edit: "))
            todos[number-1] = input("Enter the new todo: ")
        case 'complete':
            number = int(input("Enter the number for completed task: "))
            todos.pop(number-1)
        case 'exit':
            break
        case _:
            print("Yo, I don't understand what you typed!")

print('Bye!')



