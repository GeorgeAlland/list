import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("My Day")
st.subheader("Things to think about")
st.write (("Reminders and Tasks"))

for index, todo in enumerate(todos):

    info = f"({index}) {todo}"

    checkbox = st.checkbox(info, key=info)

    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)

        del st.session_state[info]

        st.rerun()

st.text_input(label="-", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')