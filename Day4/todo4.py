todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("number of todo to edit: "))
            todos[number-1] = input("Enter the new todo: ")
        case 'exit':
            break
        case _:
            print("Yo, I don't understand what you typed!")

print('Bye!')



