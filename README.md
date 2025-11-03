#  MyTasks — Gerenciador de Tarefas em Python

**Autor:** Gustavo Prates Caetano  
**Versão Atual:** 3.0 (Modularização e POO)  
**Status do Projeto:** Em desenvolvimento   

---

##  Sobre o Projeto

O **MyTasks** é um sistema de gerenciamento de tarefas desenvolvido em **Python**, criado com o objetivo de evoluir gradualmente — começando pelo terminal (CLI) e avançando até uma **API completa** com **Django** e **FastAPI**.  

Este projeto faz parte do meu plano de estudos para me tornar um **desenvolvedor back-end Python profissional**, consolidando habilidades desde os fundamentos até frameworks avançados.

---

##  Objetivo da Etapa Atual

### **Etapa 3 — Modularização e POO**
Nesta etapa, o foco é implementar a **salvaguarda e recuperação dos dados, e tambem a utilização da Programação orientada a objetos (classes e metodos),** das tarefas através de um arquivo `.json`, simulando a camada de persistência de um banco de dados.  

**Conceitos praticados:**
- Manipulação de arquivos  
- Leitura e escrita com `json.load()` e `json.dump()`  
- Tratamento de exceções (`try`, `except`)  
- Estrutura de diretórios e boas práticas de persistência  
- Criação automática de pastas (`os.makedirs`)  

**Funcionalidades:**
- Adicionar tarefa  
- Listar tarefas  
- Marcar tarefa como concluída  
- Excluir tarefa  
- **Salvar e carregar tarefas automaticamente** no arquivo `src/data/tasks.json`

---

## Etapas do Projeto

| Etapa | Versão | Descrição | Status |
|-------|---------|------------|--------|
| 1 | v1.0 | Versão CLI básica (terminal) com CRUD em memória | Concluída |
| 2 | v2.0 | Persistência em arquivo JSON | Concluída |
| 3 | v3.0 | Modularização e POO (refatoração em classes) | Concluída |
| 4 | v4.0 | Banco de dados (SQLite/PostgreSQL) | Planejada |
| 5 | v5.0 | API com Django/FastAPI | Planejada |

---

## Estrutura de Pastas

mytasks_project/
│
├── data/
│ └── tasks.json # Armazena as tarefas salvas
│
├── src/
│ └── main.py # Código principal do sistema
| └── data # Armazenar arquivo JSON
| └── Models # Armazenar arquivo task.py
| └── Service # Armazenar arquivo task_manager.py
│
└── README.md # Documentação do projeto