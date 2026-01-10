import functions
import FreeSimpleGUI as sg

label = sg.Text("Welcome to the To-Do List App!")
input_box = sg.InputText(tooltip="Enter a to-do:")
add_button = sg.Button("Add")
show_button = sg.Button("Show")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("To-Do List App", layout=[[label], [add_button, show_button, edit_button, complete_button, exit_button], [input_box]])
window.read()
window.close()