import streamlit as st
import functions

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity')


for index, todo in enumerate(todos):
    col1, col2, col3 = st.columns([1, 8, 2])  # 添加新的列用于放置删除按钮
    checkbox = col1.checkbox('', key='checkbox_' + str(index))  # 为每个复选框分配一个唯一的键
    if checkbox:
        col2.markdown(f"<s>{todo}</s>", unsafe_allow_html=True)  # 在已完成的任务上画一条线
    else:
        col2.write(todo)

    if col3.button('Delete', key='button_' + str(index)):  # 为每个按钮分配一个唯一的键
        todos.pop(index)
        functions.write_todos(todos)
        st.experimental_rerun()

# for index, todo in enumerate(todos):
#     checkbox = st.checkbox(todo, key=todo)
#     if checkbox:
#         todos.pop(index)
#         functions.write_todos(todos)
#         del st.session_state[todo]
#         st.experimental_rerun()


st.text_input(label='', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')
