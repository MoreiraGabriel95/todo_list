import os

# Functions for task management
def add_task():
    task_name = input(messages['add_task'])
    tasks.append('[ ] ' + task_name + '\n')
    save_tasks()

def list_tasks():
    print(messages['task_list'])
    for task in tasks:
        print(task, end='')
    print()

def mark_task_done():
    task_index = int(input(messages['mark_task']) ) - 1
    tasks[task_index] = tasks[task_index].replace('[ ]', '[X]')
    save_tasks()

def delete_task():
    task_index = int(input(messages['delete_task']) ) - 1
    del tasks[task_index]
    save_tasks()

def save_tasks():
    with open('tasks.txt', 'w') as file:
        file.writelines(tasks)

# Language selection
language = input("Choose a language / Escolha um idioma [EN/PT]: ")
if language.upper() == 'PT':
    messages = {
        'welcome': 'Bem-vindo(a) à sua lista de tarefas!',
        'menu': 'Escolha uma opção:\n1 - Adicionar tarefa\n2 - Listar tarefas\n3 - Marcar tarefa como concluída\n4 - Excluir tarefa\n0 - Sair\n',
        'add_task': 'Digite o nome da tarefa que deseja adicionar: ',
        'task_list': 'Lista de tarefas:',
        'mark_task': 'Digite o número da tarefa que deseja marcar como concluída: ',
        'delete_task': 'Digite o número da tarefa que deseja excluir: ',
        'goodbye': 'Obrigado por utilizar a sua lista de tarefas! Até a próxima.'
    }
else:
    messages = {
        'welcome': 'Welcome to your task list!',
        'menu': 'Choose an option:\n1 - Add task\n2 - List tasks\n3 - Mark task as done\n4 - Delete task\n0 - Quit\n',
        'add_task': 'Enter the name of the task you want to add: ',
        'task_list': 'Task list:',
        'mark_task': 'Enter the number of the task you want to mark as done: ',
        'delete_task': 'Enter the number of the task you want to delete: ',
        'goodbye': 'Thank you for using your task list! See you next time.'
    }

# Load existing tasks from file
if os.path.exists('tasks.txt'):
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()
else:
    tasks = []

# Main loop
print(messages['welcome'])
while True:
    option = input(messages['menu'])
    if option == '1':
        add_task()
    elif option == '2':
        list_tasks()
    elif option == '3':
        mark_task_done()
    elif option == '4':
        delete_task()
    elif option == '0':
        print(messages['goodbye'])
        break
    else:
        print('Invalid option.')

