

import functins
import FreeSimpleGUI as Sg

label = Sg.Text("type in a todo")
input_box = Sg.InputText(tooltip="enter a todo :")
add_button = Sg.Button("add")


my_window = Sg.Window("my to do app" , layout = [[label],[input_box , add_button]])
my_window.read()
my_window.close()
