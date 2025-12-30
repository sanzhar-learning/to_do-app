import functions

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action or "new" in user_action:
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        new_todos = [item.strip('\n') for item in todos]
        todos = new_todos
        for index, item in enumerate(todos):
            row = f"{index + 1} - {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter the new to-do item: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = functions.get_todos()

            todo_to_remove = todos[number]
            todos.pop(number)

            functions.write_todos(todos)

            message = f'The todo "{todo_to_remove.strip()}" was removed from the list.'
            print(message)
        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue
    
    elif user_action.startswith('exit'):
        try:
            break
        except ValueError:
            print("Your command is not valid.")
            continue
    else:
        print("Command not recognized.")    