import json
import os

OPEN_FILE = 'tasks.json'

def load_tasks():
    """Carrega tarefas do arquivo JSON."""
    if os.path.exists(OPEN_FILE):
        with open(OPEN_FILE, 'r') as ARQUIVS:
            return json.load(ARQUIVS)
    return {}

def save_tasks(tasks):
    """Salva tarefas no arquivo JSON."""
    with open(OPEN_FILE, 'w') as ARQUIVS:
        json.dump(tasks, ARQUIVS, indent=4)

def add_task(atvs, description, priority, category):
    """Adiciona uma nova tarefa."""
    task_id = len(atvs) + 1
    atvs[task_id] = {'description': description, 'priority': priority, 'category': category}
    save_tasks(atvs)
    print(f"Tarefa {task_id} adicionada.")

def listaTarefas(atvs):
    """Lista todas as tarefas."""
    for task_id, details in atvs.items():
        print(f"Tarefa {task_id}: {details['description']} | Prioridade: {details['priority']} | Categoria: {details['category']}")

# função principal
def main():
    atvs = load_tasks()

    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Sair")

        esc = input("informe uma opção: ")

        if esc == '1':
            description = input("Descrição da tarefa: ")
            priority = input("Prioridade (alta, média, baixa): ")
            category = input("Categoria: ")
            add_task(atvs, description, priority, category)
        elif esc == '2':
            listaTarefas(atvs)
        elif esc == '3':
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
