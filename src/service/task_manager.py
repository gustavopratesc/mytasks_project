import json
class TaskManager:
    def __init__(self) -> None:
        self.tasks = []
        self.caminho_arquivo = 'src/data/tasks.json'
        self.load_tasks()

    def load_tasks(self) -> None:
        try:
            with open(self.caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                self.tasks = json.load(arquivo)
                if not self.tasks:
                    self.tasks = []
        except FileNotFoundError:
            print('Arquivo nao encontrado, iniciando lista vazia')
            self.tasks = []
        except json.JSONDecodeError:
            print('Arquivo corrompido, reniciando lista vazia')
            self.tasks = []
        return
    
    def save_tasks(self) -> None:
        try:
            with open(self.caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(self.tasks, arquivo, indent=4)
                print('Tarefas salvas com sucesso!')
        except FileNotFoundError:
            import os 
            pasta = os.path.dirname(self.caminho_arquivo)
            os.makedirs(pasta, exist_ok=True)
            print('Pasta /data nao existia e foi criada. Salvando novamente...')
            self.save_tasks()
        except PermissionError:
            print('O sistema nao tem permissao para salvar')
        return
    
    def add_task(self, name_task) -> None:
        self.tasks.append({"name": name_task, "status": False})
        self.save_tasks()
        print(f'{name_task}: adicionada a lista!')
        print('---------------------------------')
        return
    
    def show_tasks(self) -> None:
        if not self.tasks:
            print('Nenhuma tafera adicionada ainda!')
            return
        
        for i, task in enumerate(self.tasks):
            status = "Concluida" if task["status"] else "Pendente"
            print(f'[{i + 1}]: Nome: {task["name"]} | Status: {status}')
        return
    
    def mark_as_completed(self, index_task) -> None:
        if index_task <= 0 or index_task > len(self.tasks):
            print('ERRO: Indice invalido!')
            return
        
        self.tasks[index_task - 1]["status"] = True
        self.save_tasks()
        print(f'Tarefa "{self.tasks[index_task - 1]["name"]}" marcada como concluida!!')
        return
    
    def delete_task(self, index_task) -> None:
        if index_task <= 0 or index_task > len(self.tasks):
            print('ERRO: Indice invalido!')
            return
        
        task_remove = self.tasks.pop(index_task - 1)
        self.save_tasks()
        print(f'Tarefa removida: {task_remove["name"]}')
        return