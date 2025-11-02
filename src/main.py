from time import sleep

list_tasks = []

def add_task() -> None:
    while True:
        name_task = input('Insira a tarefa: ').strip().capitalize()
        list_tasks.append({"name": name_task, "status": False})
        print(f'{name_task}: adicionada a lista!')
        print('---------------------------------')
        sleep(0.3)
        keep = input('Deseja inserir mais tarefas? [S/N]: ').strip().upper()
        if keep in ['SIM', 'S']:
            continue
        elif keep in ['NÃO', 'NAO', 'N']:
            break

def show_tasks(list_tasks: list) -> None:
    if not list_tasks:
        print('Nenhuma tarefa adicionada ainda!')
        return
    
    for i, v in enumerate(list_tasks):
        status = "Concluida" if v["status"] else "Pendente"
        print(f'[{i + 1}]: Nome: {v["name"]} | Status: {status}')

def mark_as_completed(list_tasks: list) -> None:
    if not list_tasks:
        print('Nenhuma tarefa adicionada ainda!')
        return
    
    for i, v in enumerate(list_tasks):
        print(f'[{i + 1}]: Nome: {v["name"]} | Status: {v["status"]}')
    
    try:
        task_index = int(input('Digite o indice da tarefa que quer concluir: '))
        if task_index <= 0 or task_index > len(list_tasks):
            print('ERRO: Indice invalido!')
            return
        
        list_tasks[task_index - 1]["status"] = True
        print(f'Tarefa "{list_tasks[task_index - 1]["name"]}" marcada como concluida!!')

    except ValueError:
        print('ERRO: Digite apenas números!')

def delete_task(list_tasks: list):
    if not list_tasks:
        print('Nenhuma tarefa adicionada ainda!')
        return
    print('-- DELETAR TAREFA --')
    for i, v in enumerate(list_tasks):
        print(f'[{i + 1}]: Nome: {v["name"]} | Status: {v["status"]}')

    try:
        index = int(input('Insira a posicao da tarefa: '))
        if index <= 0 or index > len(list_tasks):
            print('ERRO: Indice invalido!')
            return
        
        task_remove = list_tasks.pop(index - 1)
        print(f'Tarefa removida: {task_remove["name"]}')
    except ValueError:
        print('ERRO: Insira apenas números!')

while True:
    print(f'''
    -- MENU LISTA DE TAREFAS ---
    1- Adicionar Tarefa
    2- Listar Tarefas
    3- Marcar tarefa como concluida
    4- Excluir tarefa
    5- Sair do programa
''')
    try:
        option = int(input('Qual opção você deseja realizar?: '))
        if option > 5:
            print('ERRO: Digite apenas as opções do menu')
            continue
        
        if option == 1:
            add_task()
        elif option == 2:
            show_tasks(list_tasks)
        elif option == 3:
            mark_as_completed(list_tasks)
        elif option == 4:
            delete_task(list_tasks)
        elif option == 5:
            print('Finalizando programa...')
            sleep(0.3)
            print('Programa finalizado!')
            break
    except ValueError:
        print('Digite apenas números!')
        continue
