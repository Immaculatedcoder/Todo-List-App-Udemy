# Here is a program that as the use to add, show or exit a  todos

todos = []  # Here we create an empty list in which we would like to add our todos

while True:
    user_action = input("Type add, show, or exit: ")
    user_action = user_action.strip() # The strip is used to make account for users who include space at the end or beginning of thier text.

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case _: # The _ is an annonymous variable just incase what they entered is not part of the option
            print("Hey, you entered an unknown command!")

print("Bye")