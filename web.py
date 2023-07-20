import streamlit as st
import functions
import os
import json

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


# Load completed todos from a file
if os.path.exists('completed_todos'):
    with open('completed_todos', 'r') as f:
        completed_todos = set(json.load(f))
else:
    completed_todos = set()

todos = functions.get_todos()

st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity')

for index, todo in enumerate(todos):
    col1, col2, col3 = st.columns([1, 8, 2])  # set the delete button's size
    completed = todo in completed_todos
    checkbox = col1.checkbox('', key='checkbox_' + str(index), value=completed)
    if checkbox:
        col2.markdown(f"<s>{todo}</s>", unsafe_allow_html=True)
        completed_todos.add(todo)
    else:
        col2.write(todo)
        completed_todos.discard(todo)

    if col3.button('Delete', key='button_' + str(index)):
        todos.pop(index)
        functions.write_todos(todos)
        st.experimental_rerun()

# Save completed todos to a file
with open('completed_todos', 'w') as f:
    json.dump(list(completed_todos), f)

# for index, todo in enumerate(todos):
#     checkbox = st.checkbox(todo, key=todo)
#     if checkbox:
#         todos.pop(index)
#         functions.write_todos(todos)
#         del st.session_state[todo]
#         st.experimental_rerun()


st.text_input(label='', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')
