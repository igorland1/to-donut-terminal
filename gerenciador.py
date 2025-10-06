# Gerenciador de Lista de Tarefas

def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"nome": nome_tarefa, "concluida": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} adicionada!")
    return

def ver_tarefas(tarefas): 
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["concluida"] else " "
        nome_tarefa = tarefa["nome"]
        print(f"{indice}. [{status}] {tarefa['nome']}")

def atualizar_tarefa(tarefas, indice, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["nome"] = novo_nome_tarefa
        print(f"\nTarefa {indice} atualizada para {novo_nome_tarefa}!")
    else:
        print("\nÍndice inválido.")
    return

def concluir_tarefa(tarefas, indice):
    indice_tarefa_ajustado = int(indice) - 1
    tarefas[indice_tarefa_ajustado]["concluida"] = True
    print(f"\nTarefa {indice} concluída!")
    return

def remover_tarefas_concluidas(tarefas):
    print("\nTarefas concluídas removidas!")
    for tarefa in tarefas[:]:
        if tarefa["concluida"]:
            tarefas.remove(tarefa)
    return

tarefas = []
while True:
    print("\nMenu do Gerenciador de Lista de Tarefas")
    print("\n[1] Adicionar Tarefa")
    print("[2] Ver Tarefas")
    print("[3] Atualizar Tarefa")
    print("[4] Concluir Tarefa")
    print("[5] Remover Tarefas Concluídas")
    print("[6] Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        nome_tarefa = input("\nDigite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    
    elif opcao == '2':
        if not tarefas:
            print("\nNenhuma tarefa disponível.")
        ver_tarefas(tarefas)
    
    elif opcao == '3':
        print("\nEscolha a tarefa que deseja atualizar:")
        ver_tarefas(tarefas)
        indice = int(input("\nDigite o índice da tarefa a ser atualizada: "))
        novo_nome = input("\nDigite o novo nome da tarefa: ")
        atualizar_tarefa(tarefas, indice, novo_nome)
    
    elif opcao == '4':
        ver_tarefas(tarefas)
        indice = int(input("\nDigite o índice da tarefa a ser concluída: "))
        concluir_tarefa(tarefas, indice)
    
    elif opcao == '5':
        remover_tarefas_concluidas(tarefas)
        ver_tarefas(tarefas)
    
    elif opcao == '6':
        print("\nSaindo do gerenciador de tarefas...")
        break