#todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"   # Here we concatenate the strings so that print("text\n" ) can go onto the next line.

            file = open('todos.txt', 'r')
            todos = file.readlines()  # Here we are creating a list variable "todos" which contains data from text file.
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos) # Here we write back into the text file "Todos"
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # One Way
            # new_todos = []
            #
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            # Another Way, List comprehension

            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos): # The enumerate returns a tuple  containing a tuple as in (index, item)
                item = item.strip('\n')
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



