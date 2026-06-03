

import functions
import FreeSimpleGUI as Sg

label = Sg.Text("type in a todo")
input_box = Sg.InputText(tooltip="enter a todo :" , key="todo")
add_button = Sg.Button("Add")


my_window = Sg.Window("my to do" ,
                      layout = [[label],[input_box , add_button]] ,
                      font=("Arial", 20),)

while True:
    event, value = my_window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case Sg.WINDOW_CLOSED:
            break
my_window.close()
