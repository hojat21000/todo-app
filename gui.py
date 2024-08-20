import asd.mud as asdd

import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
     with open("todos.txt", "w")as file:
         pass

sg.theme("DarkTeal9")


clock=sg.Text("", key="clock")

label=sg.Text("type in a todo")

input_box=sg.InputText(tooltip="Enter todo" , key="todo")
add_button=sg.Button(size=20,image_size=(80,35), image_source="complete.png " ,button_color="white ",  key="Add")
list_box=sg.Listbox(values=asdd.get_todos(),key="todos",
                    enable_events=True, size=[24,12])
edit_buttn=sg.Button("Edit")
complete_button=sg.Button("Complete")
exit_button=sg.Button("Exit")

window=sg.Window("MY ToDo App" ,
                          layout=[
                              [clock],
                              [label],
                              [input_box, add_button],
                              [[list_box, edit_buttn,complete_button]],
                              [exit_button]
                          ],
                          font=("Helvtica",20,))
while True:

   event , values=window.read(timeout=10)
   window["clock"].Update(value=time.strftime("%a, %d %b %Y %H:%M:%S"))
   # print(event, values)
   print(1,event)
   print(2,values)
   print(3,values["todos"])
   # print(4,todos[index])
   match event:
       case "Add":
           todos=asdd.get_todos()
           new_todo=values["todo"]+"\n"
           todos.append(new_todo)
           asdd.set_todos(todos)
           window["todos"].update(values=todos)
       case "Edit":
            try:
               todo_to_edit=values["todos"][0]
               new_todo=values["todo"]+"\n"
               todos=asdd.get_todos()
               index=todos.index(todo_to_edit)
               todos[index]=new_todo
               asdd.set_todos(todos)
               window["todo"].update(value=" ")
               window["todos"].update(values=todos)
            except IndexError:
                sg.popup("something went wrong" ,font=("Helvetica",20))
       case "todos":
          window["todo"].update(value = values["todos"][0])

       case "Complete":
                 try:
                       todo_to_complete= values["todos"][0]
                       todos = asdd.get_todos()
                       index = todos.index(todo_to_complete)
                       todos.pop(index)
                       # todos.remove(todo_to_complete)
                       asdd.set_todos(todos)
                       window["todo"].update(value = " ")
                       window["todos"].update(values =todos)
                 except indexError:

                     sg.popup("something went wrong", font=("Helvetica", 20))
       case "exit":
           break
       case sg.WIN_CLOSED:
           exit()
# window.close()












































# import function
# import PySimpleGUI
#
# label1=PySimpleGUI.Text("type in a todo")
# input_box1=PySimpleGUI.InputText(tooltip="Enter todo")
# add_button1=PySimpleGUI.Button("Add")
#
#
# label2=PySimpleGUI.Text("number edit in a todo")
# input_box2=PySimpleGUI.InputText(tooltip="Enter a number of edit")
# add_button2=PySimpleGUI.Button("Edit")
#
#
# window1=PySimpleGUI.Window("MY ToDo App" , layout=[[label1],[input_box1, add_button1],
#                                                    [label2],[input_box2, add_button2],
#                                                    [label3],[input_box3, add_button3]])
#
# window2=PySimpleGUI.Window("MY  Edit ToDo " , layout=[[label2],[input_box2, add_button2]])
# window1.read()
# window1.close()


#   label2=PySimpleGUI.Text("Enter a new_todo")
#   input_box2=PySimpleGUI.InputText(tooltip="Enter a neew_todo")
#   add_button2=PySimpleGUI.Button("Add")
#
#
# print("Hello")
# window3.close()
