import os
from models.task import Task
import json
class TaskManager:
    def __init__(self) -> None:
        self.tasks = []
        self.caminho_arquivo = 'src/data/tasks.json'
        self.load_tasks()

    def load_tasks(self) -> None:
        """Carrega as tarefas do arquivo JSON e reconstrói objetos Task."""
        try:
            with open(self.caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                self.tasks = [Task(**item) for item in dados] if dados else []
        except FileNotFoundError:
            print('Arquivo nao encontrado, iniciando lista vazia')
            self.tasks = []
        except json.JSONDecodeError:
            print('Arquivo corrompido, reniciando lista vazia')
            self.tasks = []
        return
    
    def save_tasks(self) -> None:
        """Salva as tarefas no arquivo JSON."""
        try:
            with open(self.caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump([t.to_dict() for t in self.tasks], arquivo, indent=4)
                print('Tarefas salvas com sucesso!')
        except FileNotFoundError:
            pasta = os.path.dirname(self.caminho_arquivo)
            os.makedirs(pasta, exist_ok=True)
            print('Pasta /data nao existia e foi criada. Salvando novamente...')
            self.save_tasks()
        except PermissionError:
            print('O sistema nao tem permissao para salvar')
        return
    
    def add_task(self, name_task) -> None:
        """Adiciona uma nova tarefa a lista."""
        # self.tasks.append({"name": name_task, "status": False})
        new_task = Task(name_task)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f'{name_task}: adicionada a lista!')
        print('---------------------------------')
        return
    
    def show_tasks(self) -> None:
        """Exibe as tarefas na tela."""        
        if not self.tasks:
            print('Nenhuma tafera adicionada ainda!')
            return
        
        for i, task in enumerate(self.tasks):
            status = "Concluida" if task.status else "Pendente"
            print(f'[{i + 1}]: Nome: {task.name} | Status: {status}')
        return
    
    def mark_as_completed(self, index_task) -> None:
        """Marca uma tarefa como concluida."""
        if index_task <= 0 or index_task > len(self.tasks):
            print('ERRO: Índice inválido!')
            return

        task = self.tasks[index_task - 1]
        task.mark_as_completed()
        self.save_tasks()
        print(f'Tarefa "{task.name}" marcada como concluída!!')
    
    def delete_task(self, index_task) -> None:
        """Remove uma tarefa da lista."""
        if index_task <= 0 or index_task > len(self.tasks):
            print('ERRO: Indice invalido!')
            return
        
        task_remove = self.tasks.pop(index_task - 1)
        self.save_tasks()
        print(f'Tarefa removida: {task_remove["name"]}')
        return