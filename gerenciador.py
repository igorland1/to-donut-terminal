# 🍩 TO-DONUT - Gerenciador de Tarefas Delicioso! 🍩
from colorama import Fore, Back, Style, init
import json
import os

# Inicializar colorama
init(autoreset=True)

# Cores tema donut
ROSA_DONUT = Fore.LIGHTMAGENTA_EX
CHOCOLATE = Fore.YELLOW
MORANGO = Fore.LIGHTRED_EX
BAUNILHA = Fore.LIGHTCYAN_EX
POLVILHO = Fore.LIGHTWHITE_EX
CARAMELO = Fore.LIGHTYELLOW_EX

# Arquivo de persistência
ARQUIVO_TAREFAS = 'tarefas.json'

def carregar_tarefas():
    """Carrega tarefas do arquivo JSON"""
    if os.path.exists(ARQUIVO_TAREFAS):
        try:
            with open(ARQUIVO_TAREFAS, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                tarefas = dados.get('tarefas', [])
                if tarefas:
                    print(f"{BAUNILHA}🍩 Carregando sua caixa de donuts... ✓{Style.RESET_ALL}")
                    print(f"{CARAMELO}🍩 {len(tarefas)} donut(s) encontrado(s)!{Style.RESET_ALL}\n")
                return tarefas
        except json.JSONDecodeError:
            print(f"{MORANGO}🍩 Ops! Arquivo corrompido. Criando caixa nova...{Style.RESET_ALL}\n")
            return []
        except Exception as e:
            print(f"{MORANGO}🍩 Erro ao carregar: {e}{Style.RESET_ALL}\n")
            return []
    return []

def salvar_tarefas(tarefas):
    """Salva tarefas no arquivo JSON"""
    try:
        with open(ARQUIVO_TAREFAS, 'w', encoding='utf-8') as arquivo:
            json.dump({'tarefas': tarefas}, arquivo, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"{MORANGO}🍩 Erro ao salvar: {e}{Style.RESET_ALL}")

def banner():
    print(f"\n{ROSA_DONUT}{'='*60}")
    print(f"{CARAMELO}   🍩  TO-DONUT  🍩  Suas tarefas nunca foram tão doces!  🍩")
    print(f"{ROSA_DONUT}{'='*60}{Style.RESET_ALL}\n")

def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"nome": nome_tarefa, "concluida": False}
    tarefas.append(tarefa)
    frases = [
        "🍩 Mmm... Tarefa fresquinha saindo do forno!",
        "🍩 Que delícia! Mais uma tarefa na bandeja!",
        "🍩 Sua lista tá crescendo como massa de donut!",
        "🍩 Polvilhada e pronta! Tarefa adicionada!"
    ]
    import random
    print(f"{MORANGO}{random.choice(frases)}{Style.RESET_ALL}")
    print(f"{POLVILHO}   → {nome_tarefa}{Style.RESET_ALL}")
    salvar_tarefas(tarefas)
    return

def ver_tarefas(tarefas):
    if not tarefas:
        print(f"{CHOCOLATE}🍩 Sua caixa de donuts está vazia! Hora de adicionar tarefas!{Style.RESET_ALL}\n")
        return

    print(f"{BAUNILHA}{'─'*60}")
    print(f"   🍩  SUA CAIXA DE DONUTS (Tarefas)  🍩")
    print(f"{'─'*60}{Style.RESET_ALL}\n")

    for indice, tarefa in enumerate(tarefas, start=1):
        if tarefa["concluida"]:
            status = "✓"
            cor = Fore.GREEN
            emoji = "🍩✨"
        else:
            status = " "
            cor = CHOCOLATE
            emoji = "🍩"
        nome_tarefa = tarefa["nome"]
        print(f"{cor}{emoji} {indice}. [{status}] {nome_tarefa}{Style.RESET_ALL}")

def atualizar_tarefa(tarefas, indice, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["nome"] = novo_nome_tarefa
        print(f"{BAUNILHA}🍩 Donut reformulado! Nova receita aplicada!{Style.RESET_ALL}")
        print(f"{POLVILHO}   → {novo_nome_tarefa}{Style.RESET_ALL}")
        salvar_tarefas(tarefas)
    else:
        print(f"{MORANGO}🍩 Ops! Esse donut não existe na caixa...{Style.RESET_ALL}")
    return

def concluir_tarefa(tarefas, indice):
    indice_tarefa_ajustado = int(indice) - 1
    tarefas[indice_tarefa_ajustado]["concluida"] = True
    frases = [
        "🍩✨ Nhac! Donut devorado com sucesso!",
        "🍩✨ Que sabor maravilhoso! Tarefa concluída!",
        "🍩✨ Delicioso! Mais um donut saboreado!",
        "🍩✨ Mmm... Esse tava uma delícia! Concluído!"
    ]
    import random
    print(f"{Fore.GREEN}{random.choice(frases)}{Style.RESET_ALL}")
    salvar_tarefas(tarefas)
    return

def remover_tarefas_concluidas(tarefas):
    count = sum(1 for t in tarefas if t["concluida"])
    for tarefa in tarefas[:]:
        if tarefa["concluida"]:
            tarefas.remove(tarefa)
    if count > 0:
        print(f"{CARAMELO}🍩 Limpando as migalhas... {count} donut(s) removido(s)!{Style.RESET_ALL}")
        salvar_tarefas(tarefas)
    else:
        print(f"{CHOCOLATE}🍩 Nenhuma migalha pra limpar! Caixa já está limpa!{Style.RESET_ALL}")
    return

# Mostrar banner inicial
banner()

# Carregar tarefas salvas
tarefas = carregar_tarefas()

while True:
    print(f"\n{ROSA_DONUT}╔══════════════════════════════════════════════════════════╗")
    print(f"║        🍩  MENU DA DOCERIA TO-DONUT  🍩                  ║")
    print(f"╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n")
    print(f"{CARAMELO}[1]🍩 Adicionar Donut (Nova Tarefa){Style.RESET_ALL}")
    print(f"{BAUNILHA}[2]🍩 Ver Caixa de Donuts (Listar Tarefas){Style.RESET_ALL}")
    print(f"{CHOCOLATE}[3]🍩 Mudar Sabor (Atualizar Tarefa){Style.RESET_ALL}")
    print(f"{Fore.GREEN}[4]🍩 Devorar Donut (Concluir Tarefa){Style.RESET_ALL}")
    print(f"{MORANGO}[5]🍩 Limpar Migalhas (Remover Concluídas){Style.RESET_ALL}")
    print(f"{Fore.RED}[6]🍩 Fechar a Doceria (Sair){Style.RESET_ALL}")

    opcao = input(f"\n{POLVILHO}🍩 Escolha seu donut: {Style.RESET_ALL}")

    if opcao == '1':
        nome_tarefa = input(f"\n{CARAMELO}🍩 Que sabor de donut você quer criar? {Style.RESET_ALL}")
        adicionar_tarefa(tarefas, nome_tarefa)

    elif opcao == '2':
        ver_tarefas(tarefas)

    elif opcao == '3':
        ver_tarefas(tarefas)
        if tarefas:
            indice = int(input(f"\n{CHOCOLATE}🍩 Qual donut quer mudar? (número): {Style.RESET_ALL}"))
            novo_nome = input(f"{CHOCOLATE}🍩 Novo sabor: {Style.RESET_ALL}")
            atualizar_tarefa(tarefas, indice, novo_nome)

    elif opcao == '4':
        ver_tarefas(tarefas)
        if tarefas:
            indice = int(input(f"\n{Fore.GREEN}🍩 Qual donut você vai devorar? (número): {Style.RESET_ALL}"))
            concluir_tarefa(tarefas, indice)

    elif opcao == '5':
        remover_tarefas_concluidas(tarefas)
        ver_tarefas(tarefas)

    elif opcao == '6':
        salvar_tarefas(tarefas)
        print(f"\n{BAUNILHA}🍩 Salvando sua caixa de donuts... ✓{Style.RESET_ALL}")
        print(f"\n{ROSA_DONUT}{'='*60}")
        print(f"{CARAMELO}   🍩 Obrigado por visitar a TO-DONUT! Volte sempre! 🍩")
        print(f"{ROSA_DONUT}{'='*60}{Style.RESET_ALL}\n")
        break

    else:
        print(f"{MORANGO}🍩 Ops! Esse sabor não existe no cardápio!{Style.RESET_ALL}")