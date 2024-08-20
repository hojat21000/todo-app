import streamlit as st
import mud

todos=mud.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increasee your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
