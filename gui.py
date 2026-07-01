from turtledemo import clock

import FreeSimpleGUI as Sg
import functions
import time

Sg.theme("DarkGrey2")
label = Sg.Text("type in a todo")
input_box = Sg.InputText(tooltip="enter a todo :" , key="todo")
add_button = Sg.Button("Add")
list_box = Sg.Listbox(key="todos" , size = (45, 10) , values=functions.get_todos() , enable_events=True )
edit_button = Sg.Button("Edit")
exit_button = Sg.Button("Exit")
complete_button = Sg.Button("Complete")
clock1 = Sg.Text(" " , key="clock")


my_window = Sg.Window("my to do" ,
                      layout = [[clock1],
                                [label],
                                [input_box , add_button] ,
                                [list_box , edit_button , complete_button] ,
                                [exit_button]] ,
                      font=("Arial", 20),)

while True:
    event, values = my_window.read(timeout=200)
    my_window["clock"].update(value=time.strftime("%H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            my_window["todos"].update(values= todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"
                todos = functions.get_todos()
                index =todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                my_window["todos"].update(values=todos)
                my_window["todo"].update(value="")
            except IndexError:
                Sg.popup("select an item first" , font=("Arial", 20))

        case "todos" :
            my_window["todo"].update(value=values["todos"][0])

        case "Exit" :
            break

        case "Complete" :
            try:
                todos = functions.get_todos()
                item_to_remove  = values["todos"][0]
                todos.remove(item_to_remove)
                functions.write_todos(todos)
                my_window["todos"].update(values=todos)
                my_window["todo"].update(value="")
            except IndexError:
                Sg.popup("select an item first" , font=("Arial", 20))
        case Sg.WINDOW_CLOSED:
            break
my_window.close()
