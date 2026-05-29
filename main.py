from functins import write_todos, get_todos
import time

now = time.strftime('%a %d %b %Y, %I:%M%p')
print(now)

while True:
    user_action = input("What do you want to do?"
                     "\n1 . Add  "
                     "\n2 . show "
                     "\n3 . edit "
                     "\n4 . finished"
                     "\n5 . exit ")
    user_action = user_action.strip()


    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")
        write_todos(todos)

        write_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos()


        new_todos = [item.strip("\n") for item in todos]

        for index , item in enumerate(new_todos):
            print(f"{index+1}. {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[4:])
            number = number - 1

            todos = get_todos()

            new_todo = input("enter a new todo :")
            todos[number] =  new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print("Please enter a valid input")
            continue
        except IndexError:
            print("the number you entered does not exist")
            continue


    elif user_action.startswith("finished") :
        try:
            number = int(input("enter the number of the task you want to remove as finished: "))
            number = number - 1

            todos = get_todos()

            todos.pop(number)

            write_todos(todos)
        except IndexError:
            print("the number you entered does not exist")
            continue

        message_number = number + 1
        message = f"the todo number {message_number} has been removed successfully"
        print(message)
    elif user_action.startswith("exit") :
        print("Goodbye")
        break
    else :
        print("Please enter a valid input")


