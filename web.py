import streamlit as st
import mud

todos=mud.get_todos()

def add_todo():
    # todos = mud.get_todos()
    todo=st.session_state["new_todo"]
    todos.append(todo + "\n")
    mud.set_todos(todos)

def remove_todo(todo):
    todos.remove(todo)
    mud.set_todos(todos)
    st.rerun()


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increasee your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"checkbox_{index}")
    if checkbox:
        remove_todo(todo)


st.text_input(label="", placeholder="Enter new todo: " ,
            on_change=add_todo,key="new_todo" )
print("hello")

st.session_state

st.session_state["new_todo"]
