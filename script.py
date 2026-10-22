def exibir_menu():
    print("\n" + "="*30)
    print("  GERENCIADOR DE TAREFAS")
    print("="*30)
    print("1. Visualizar tarefas")
    print("2. Adicionar nova tarefa")
    print("3. Remover uma tarefa")
    print("4. Sair")
    print("="*30)

def gerenciar_tarefas():
    tarefas = ["Estudar Python", "Configurar repositório Git", "Revisar matéria"]
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            print("\n--- Suas Tarefas ---")
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa}")
                    
        elif opcao == "2":
            nova_tarefa = input("\nDigite o nome da nova tarefa: ").strip()
            if nova_tarefa:
                tarefas.append(nova_tarefa)
                print(f"Tarefa '{nova_tarefa}' adicionada com sucesso!")
            else:
                print("Aviso: O nome da tarefa não pode ser vazio.")
                
        elif opcao == "3":
            print("\n--- Remover Tarefa ---")
            if not tarefas:
                print("Não há tarefas para remover.")
            else:
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa}")
                try:
                    indice = int(input("\nDigite o número da tarefa que deseja remover: "))
                    if 1 <= indice <= len(tarefas):
                        removida = tarefas.pop(indice - 1)
                        print(f"Tarefa '{removida}' removida com sucesso!")
                    else:
                        print("Erro: Número inválido.")
                except ValueError:
                    print("Erro: Por favor, digite um número inteiro válido.")
                    
        elif opcao == "4":
            print("\nObrigado por usar o Gerenciador de Tarefas! Até logo.")
            break
        else:
            print("Opção inválida! Escolha um número de 1 a 4.")

if __name__ == "__main__":
    gerenciar_tarefas()
