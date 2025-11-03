import os
from service.task_manager import TaskManager
from time import sleep

gerenciador = TaskManager()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    

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
        match option:
            case 1:
                name_task = input('Digite o nome da tarefa: ').strip().capitalize()
                gerenciador.add_task(name_task)
            case 2:
                limpar_tela()
                gerenciador.show_tasks()
            case 3:
                task_index = int(input('Digite o indice da tarefa: '))
                gerenciador.mark_as_completed(task_index)
            case 4:
                task_index = int(input('Digite o indice da tarefa: '))
                gerenciador.delete_task(task_index)
            case 5:
                print('Finalizando programa...')
                sleep(0.3)
                print('Programa finalizado!')
                break          
    except ValueError:
        print('Digite apenas números!')
        continue
