# 🍩 TO-DONUT - Gerenciador de Tarefas Delicioso! 🍩
from colorama import Fore, Back, Style, init
import json
import os
from datetime import datetime
import random

# Inicializar colorama
init(autoreset=True)

# Cores tema donut
ROSA_DONUT = Fore.LIGHTMAGENTA_EX
CHOCOLATE = Fore.YELLOW
MORANGO = Fore.LIGHTRED_EX
BAUNILHA = Fore.LIGHTCYAN_EX
POLVILHO = Fore.LIGHTWHITE_EX
CARAMELO = Fore.LIGHTYELLOW_EX

# Arquivos de persistência
ARQUIVO_TAREFAS = 'tarefas.json'
ARQUIVO_STATS = 'stats.json'

# Prioridades (sabores de donuts)
PRIORIDADES = {
    'chocolate': {'emoji': '🍫', 'cor': Fore.RED, 'nome': 'Chocolate (Urgente)'},
    'morango': {'emoji': '🍓', 'cor': Fore.LIGHTRED_EX, 'nome': 'Morango (Importante)'},
    'baunilha': {'emoji': '🍦', 'cor': Fore.LIGHTYELLOW_EX, 'nome': 'Baunilha (Normal)'},
    'cookies': {'emoji': '🍪', 'cor': Fore.LIGHTCYAN_EX, 'nome': 'Cookies (Baixa)'}
}

# Conquistas disponíveis
CONQUISTAS = {
    'primeiro_sabor': {'nome': '🥇 Primeiro Sabor', 'desc': 'Complete sua primeira tarefa', 'meta': 1},
    'doceiro_iniciante': {'nome': '🍩 Doceiro Iniciante', 'desc': 'Crie 10 tarefas', 'meta': 10},
    'comedor_voraz': {'nome': '⚡ Comedor Voraz', 'desc': 'Complete 5 tarefas em 1 dia', 'meta': 5},
    'sequencia_doce': {'nome': '🔥 Sequência Doce', 'desc': 'Use o app por 7 dias seguidos', 'meta': 7},
    'mestre_confeiteiro': {'nome': '👑 Mestre Confeiteiro', 'desc': 'Complete 100 tarefas', 'meta': 100},
    'organizador': {'nome': '🏷️ Organizador', 'desc': 'Use tags em 10 tarefas', 'meta': 10}
}

def carregar_stats():
    """Carrega estatísticas do arquivo JSON"""
    if os.path.exists(ARQUIVO_STATS):
        try:
            with open(ARQUIVO_STATS, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except:
            pass
    return {
        'total_criadas': 0,
        'total_concluidas': 0,
        'ultimo_acesso': datetime.now().strftime('%Y-%m-%d'),
        'dias_sequencia': 1,
        'conquistas_desbloqueadas': [],
        'historico_conclusoes': {}
    }

def salvar_stats(stats):
    """Salva estatísticas no arquivo JSON"""
    try:
        with open(ARQUIVO_STATS, 'w', encoding='utf-8') as arquivo:
            json.dump(stats, arquivo, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"{MORANGO}🍩 Erro ao salvar estatísticas: {e}{Style.RESET_ALL}")

def atualizar_sequencia(stats):
    """Atualiza sequência de dias"""
    hoje = datetime.now().strftime('%Y-%m-%d')
    ultimo = stats.get('ultimo_acesso', hoje)

    if ultimo != hoje:
        # Calcula diferença de dias
        data_ultimo = datetime.strptime(ultimo, '%Y-%m-%d')
        data_hoje = datetime.strptime(hoje, '%Y-%m-%d')
        diff = (data_hoje - data_ultimo).days

        if diff == 1:
            stats['dias_sequencia'] += 1
        elif diff > 1:
            stats['dias_sequencia'] = 1

        stats['ultimo_acesso'] = hoje
        salvar_stats(stats)

def verificar_conquistas(stats, tarefas):
    """Verifica e desbloqueia conquistas"""
    novas = []
    desbloqueadas = stats.get('conquistas_desbloqueadas', [])

    # Primeiro Sabor
    if 'primeiro_sabor' not in desbloqueadas and stats['total_concluidas'] >= 1:
        novas.append('primeiro_sabor')

    # Doceiro Iniciante
    if 'doceiro_iniciante' not in desbloqueadas and stats['total_criadas'] >= 10:
        novas.append('doceiro_iniciante')

    # Mestre Confeiteiro
    if 'mestre_confeiteiro' not in desbloqueadas and stats['total_concluidas'] >= 100:
        novas.append('mestre_confeiteiro')

    # Sequência Doce
    if 'sequencia_doce' not in desbloqueadas and stats.get('dias_sequencia', 0) >= 7:
        novas.append('sequencia_doce')

    # Organizador
    tarefas_com_tags = sum(1 for t in tarefas if t.get('tags', []))
    if 'organizador' not in desbloqueadas and tarefas_com_tags >= 10:
        novas.append('organizador')

    # Comedor Voraz
    hoje = datetime.now().strftime('%Y-%m-%d')
    conclusoes_hoje = stats.get('historico_conclusoes', {}).get(hoje, 0)
    if 'comedor_voraz' not in desbloqueadas and conclusoes_hoje >= 5:
        novas.append('comedor_voraz')

    # Adicionar novas conquistas e mostrar
    for conquista in novas:
        stats['conquistas_desbloqueadas'].append(conquista)
        info = CONQUISTAS[conquista]
        print(f"\n{Fore.YELLOW}{'='*60}")
        print(f"🏆 CONQUISTA DESBLOQUEADA! 🏆")
        print(f"{info['nome']}")
        print(f"{info['desc']}")
        print(f"{'='*60}{Style.RESET_ALL}\n")

    if novas:
        salvar_stats(stats)

def carregar_tarefas():
    """Carrega tarefas do arquivo JSON"""
    if os.path.exists(ARQUIVO_TAREFAS):
        try:
            with open(ARQUIVO_TAREFAS, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                tarefas = dados.get('tarefas', [])

                # Migração: adicionar campos novos em tarefas antigas
                for tarefa in tarefas:
                    if 'prioridade' not in tarefa:
                        tarefa['prioridade'] = 'baunilha'
                    if 'tags' not in tarefa:
                        tarefa['tags'] = []
                    if 'data_criacao' not in tarefa:
                        tarefa['data_criacao'] = datetime.now().strftime('%Y-%m-%d')
                    if 'data_conclusao' not in tarefa:
                        tarefa['data_conclusao'] = None

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

def adicionar_tarefa(tarefas, stats):
    nome_tarefa = input(f"\n{CARAMELO}🍩 Que sabor de donut você quer criar? {Style.RESET_ALL}")

    # Escolher prioridade
    print(f"\n{POLVILHO}Escolha a prioridade (sabor):{Style.RESET_ALL}")
    print(f"{Fore.RED}[1] 🍫 Chocolate (Urgente){Style.RESET_ALL}")
    print(f"{MORANGO}[2] 🍓 Morango (Importante){Style.RESET_ALL}")
    print(f"{CARAMELO}[3] 🍦 Baunilha (Normal){Style.RESET_ALL}")
    print(f"{BAUNILHA}[4] 🍪 Cookies (Baixa){Style.RESET_ALL}")

    prioridade_map = {'1': 'chocolate', '2': 'morango', '3': 'baunilha', '4': 'cookies'}
    prioridade_escolha = input(f"{POLVILHO}Prioridade [1-4, padrão 3]: {Style.RESET_ALL}") or '3'
    prioridade = prioridade_map.get(prioridade_escolha, 'baunilha')

    # Adicionar tags
    print(f"\n{POLVILHO}Tags (separe por vírgula, ex: trabalho,urgente):{Style.RESET_ALL}")
    tags_input = input(f"{POLVILHO}Tags (ou Enter para pular): {Style.RESET_ALL}")
    tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()]

    tarefa = {
        "nome": nome_tarefa,
        "concluida": False,
        "prioridade": prioridade,
        "tags": tags,
        "data_criacao": datetime.now().strftime('%Y-%m-%d'),
        "data_conclusao": None
    }
    tarefas.append(tarefa)

    frases = [
        "🍩 Mmm... Tarefa fresquinha saindo do forno!",
        "🍩 Que delícia! Mais uma tarefa na bandeja!",
        "🍩 Sua lista tá crescendo como massa de donut!",
        "🍩 Polvilhada e pronta! Tarefa adicionada!"
    ]

    print(f"\n{MORANGO}{random.choice(frases)}{Style.RESET_ALL}")
    prior_info = PRIORIDADES[prioridade]
    print(f"{prior_info['cor']}{prior_info['emoji']} → {nome_tarefa}{Style.RESET_ALL}")
    if tags:
        print(f"{BAUNILHA}   Tags: {', '.join(['#'+t for t in tags])}{Style.RESET_ALL}")

    stats['total_criadas'] += 1
    salvar_tarefas(tarefas)
    salvar_stats(stats)
    verificar_conquistas(stats, tarefas)

def ver_tarefas(tarefas, filtro_tag=None):
    tarefas_filtradas = tarefas

    if filtro_tag:
        tarefas_filtradas = [t for t in tarefas if filtro_tag in t.get('tags', [])]
        if not tarefas_filtradas:
            print(f"{MORANGO}🍩 Nenhum donut encontrado com a tag #{filtro_tag}!{Style.RESET_ALL}\n")
            return

    if not tarefas_filtradas:
        print(f"{CHOCOLATE}🍩 Sua caixa de donuts está vazia! Hora de adicionar tarefas!{Style.RESET_ALL}\n")
        return

    print(f"{BAUNILHA}{'─'*60}")
    if filtro_tag:
        print(f"   🍩  DONUTS COM TAG #{filtro_tag}  🍩")
    else:
        print(f"   🍩  SUA CAIXA DE DONUTS (Tarefas)  🍩")
    print(f"{'─'*60}{Style.RESET_ALL}\n")

    for indice, tarefa in enumerate(tarefas, start=1):
        if filtro_tag and filtro_tag not in tarefa.get('tags', []):
            continue

        prior = tarefa.get('prioridade', 'baunilha')
        prior_info = PRIORIDADES[prior]

        if tarefa["concluida"]:
            status = "✓"
            cor = Fore.GREEN
            emoji = "🍩✨"
        else:
            status = " "
            cor = prior_info['cor']
            emoji = prior_info['emoji']

        nome_tarefa = tarefa["nome"]
        tags = tarefa.get('tags', [])
        tags_str = f" {BAUNILHA}[{', '.join(['#'+t for t in tags])}]{Style.RESET_ALL}" if tags else ""

        print(f"{cor}{emoji} {indice}. [{status}] {nome_tarefa}{tags_str}{Style.RESET_ALL}")

def atualizar_tarefa(tarefas, indice, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["nome"] = novo_nome_tarefa
        print(f"{BAUNILHA}🍩 Donut reformulado! Nova receita aplicada!{Style.RESET_ALL}")
        print(f"{POLVILHO}   → {novo_nome_tarefa}{Style.RESET_ALL}")
        salvar_tarefas(tarefas)
    else:
        print(f"{MORANGO}🍩 Ops! Esse donut não existe na caixa...{Style.RESET_ALL}")

def concluir_tarefa(tarefas, indice, stats):
    indice_tarefa_ajustado = int(indice) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["concluida"] = True
        tarefas[indice_tarefa_ajustado]["data_conclusao"] = datetime.now().strftime('%Y-%m-%d')

        frases = [
            "🍩✨ Nhac! Donut devorado com sucesso!",
            "🍩✨ Que sabor maravilhoso! Tarefa concluída!",
            "🍩✨ Delicioso! Mais um donut saboreado!",
            "🍩✨ Mmm... Esse tava uma delícia! Concluído!"
        ]
        print(f"{Fore.GREEN}{random.choice(frases)}{Style.RESET_ALL}")

        # Atualizar estatísticas
        stats['total_concluidas'] += 1
        hoje = datetime.now().strftime('%Y-%m-%d')
        historico = stats.get('historico_conclusoes', {})
        historico[hoje] = historico.get(hoje, 0) + 1
        stats['historico_conclusoes'] = historico

        salvar_tarefas(tarefas)
        salvar_stats(stats)
        verificar_conquistas(stats, tarefas)
    else:
        print(f"{MORANGO}🍩 Ops! Esse donut não existe na caixa...{Style.RESET_ALL}")

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

def mostrar_dashboard(stats, tarefas):
    """Mostra dashboard com estatísticas"""
    pendentes = sum(1 for t in tarefas if not t["concluida"])
    concluidas_lista = sum(1 for t in tarefas if t["concluida"])
    total_lista = len(tarefas)

    taxa_conclusao = (stats['total_concluidas'] / stats['total_criadas'] * 100) if stats['total_criadas'] > 0 else 0

    print(f"\n{ROSA_DONUT}{'='*60}")
    print(f"{'  ':^60}")
    print(f"{'📊  DASHBOARD DA DOCERIA TO-DONUT  📊':^60}")
    print(f"{'  ':^60}")
    print(f"{'='*60}{Style.RESET_ALL}\n")

    print(f"{CARAMELO}📦 ESTATÍSTICAS GERAIS:{Style.RESET_ALL}")
    print(f"   {POLVILHO}Total de donuts criados: {stats['total_criadas']}{Style.RESET_ALL}")
    print(f"   {CHOCOLATE}Donuts frescos (pendentes): {pendentes}{Style.RESET_ALL}")
    print(f"   {Fore.GREEN}Donuts saboreados (concluídos): {stats['total_concluidas']}{Style.RESET_ALL}")
    print(f"   {BAUNILHA}Donuts na caixa atual: {total_lista}{Style.RESET_ALL}")
    print(f"   {MORANGO}Taxa de conclusão: {taxa_conclusao:.1f}%{Style.RESET_ALL}")
    print(f"   {CARAMELO}🔥 Sequência atual: {stats.get('dias_sequencia', 1)} dia(s){Style.RESET_ALL}")

    # Estatísticas por prioridade
    print(f"\n{BAUNILHA}🍩 DONUTS POR SABOR (Prioridade):{Style.RESET_ALL}")
    for key, info in PRIORIDADES.items():
        count = sum(1 for t in tarefas if t.get('prioridade') == key and not t['concluida'])
        if count > 0:
            print(f"   {info['cor']}{info['emoji']} {info['nome']}: {count}{Style.RESET_ALL}")

    # Tags mais usadas
    todas_tags = {}
    for t in tarefas:
        for tag in t.get('tags', []):
            todas_tags[tag] = todas_tags.get(tag, 0) + 1

    if todas_tags:
        print(f"\n{POLVILHO}🏷️  TAGS MAIS USADAS:{Style.RESET_ALL}")
        top_tags = sorted(todas_tags.items(), key=lambda x: x[1], reverse=True)[:5]
        for tag, count in top_tags:
            print(f"   {BAUNILHA}#{tag}: {count} tarefa(s){Style.RESET_ALL}")

    # Barra de progresso
    if total_lista > 0:
        progresso = int((concluidas_lista / total_lista) * 10)
        barra = "🍩" * progresso + "▢" * (10 - progresso)
        print(f"\n{CARAMELO}Progresso da caixa atual:{Style.RESET_ALL}")
        print(f"   {barra} {concluidas_lista}/{total_lista} ({concluidas_lista/total_lista*100:.0f}%)")

    print(f"\n{ROSA_DONUT}{'='*60}{Style.RESET_ALL}\n")

def mostrar_conquistas(stats):
    """Mostra conquistas desbloqueadas e bloqueadas"""
    desbloqueadas = stats.get('conquistas_desbloqueadas', [])

    print(f"\n{ROSA_DONUT}{'='*60}")
    print(f"{'🏆  SUAS CONQUISTAS  🏆':^60}")
    print(f"{'='*60}{Style.RESET_ALL}\n")

    print(f"{Fore.GREEN}✅ DESBLOQUEADAS ({len(desbloqueadas)}/{len(CONQUISTAS)}):{Style.RESET_ALL}\n")
    for key in desbloqueadas:
        if key in CONQUISTAS:
            info = CONQUISTAS[key]
            print(f"   {Fore.GREEN}{info['nome']}{Style.RESET_ALL}")
            print(f"   {POLVILHO}{info['desc']}{Style.RESET_ALL}\n")

    print(f"{CHOCOLATE}🔒 BLOQUEADAS:{Style.RESET_ALL}\n")
    for key, info in CONQUISTAS.items():
        if key not in desbloqueadas:
            print(f"   {CHOCOLATE}{info['nome']}{Style.RESET_ALL}")
            print(f"   {POLVILHO}{info['desc']}{Style.RESET_ALL}\n")

    print(f"{ROSA_DONUT}{'='*60}{Style.RESET_ALL}\n")

def buscar_por_tag(tarefas):
    """Busca tarefas por tag"""
    print(f"\n{BAUNILHA}Tags disponíveis:{Style.RESET_ALL}")
    todas_tags = set()
    for t in tarefas:
        todas_tags.update(t.get('tags', []))

    if not todas_tags:
        print(f"{MORANGO}🍩 Nenhuma tag encontrada! Adicione tags às suas tarefas.{Style.RESET_ALL}\n")
        return

    for tag in sorted(todas_tags):
        count = sum(1 for t in tarefas if tag in t.get('tags', []))
        print(f"   {BAUNILHA}#{tag} ({count}){Style.RESET_ALL}")

    tag_busca = input(f"\n{POLVILHO}Digite a tag para buscar (sem #): {Style.RESET_ALL}")
    if tag_busca:
        ver_tarefas(tarefas, filtro_tag=tag_busca)

# Mostrar banner inicial
banner()

# Carregar tarefas e estatísticas
tarefas = carregar_tarefas()
stats = carregar_stats()
atualizar_sequencia(stats)

while True:
    print(f"\n{ROSA_DONUT}╔══════════════════════════════════════════════════════════╗")
    print(f"║        🍩  MENU DA DOCERIA TO-DONUT  🍩                  ║")
    print(f"╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n")
    print(f"{CARAMELO}[1] 🍩 Adicionar Donut (Nova Tarefa){Style.RESET_ALL}")
    print(f"{BAUNILHA}[2] 🍩 Ver Caixa de Donuts (Listar Tarefas){Style.RESET_ALL}")
    print(f"{CHOCOLATE}[3] 🍩 Mudar Sabor (Atualizar Tarefa){Style.RESET_ALL}")
    print(f"{Fore.GREEN}[4] 🍩 Devorar Donut (Concluir Tarefa){Style.RESET_ALL}")
    print(f"{MORANGO}[5] 🍩 Limpar Migalhas (Remover Concluídas){Style.RESET_ALL}")
    print(f"{POLVILHO}[6] 🏷️  Buscar por Tag{Style.RESET_ALL}")
    print(f"{CARAMELO}[7] 📊 Dashboard (Estatísticas){Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[8] 🏆 Conquistas{Style.RESET_ALL}")
    print(f"{Fore.RED}[9] 🍩 Fechar a Doceria (Sair){Style.RESET_ALL}")

    opcao = input(f"\n{POLVILHO}🍩 Escolha seu donut: {Style.RESET_ALL}")

    if opcao == '1':
        adicionar_tarefa(tarefas, stats)

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
            concluir_tarefa(tarefas, indice, stats)

    elif opcao == '5':
        remover_tarefas_concluidas(tarefas)
        ver_tarefas(tarefas)

    elif opcao == '6':
        buscar_por_tag(tarefas)

    elif opcao == '7':
        mostrar_dashboard(stats, tarefas)

    elif opcao == '8':
        mostrar_conquistas(stats)

    elif opcao == '9':
        salvar_tarefas(tarefas)
        salvar_stats(stats)
        print(f"\n{BAUNILHA}🍩 Salvando sua caixa de donuts... ✓{Style.RESET_ALL}")
        print(f"\n{ROSA_DONUT}{'='*60}")
        print(f"{CARAMELO}   🍩 Obrigado por visitar a TO-DONUT! Volte sempre! 🍩")
        print(f"{ROSA_DONUT}{'='*60}{Style.RESET_ALL}\n")
        break

    else:
        print(f"{MORANGO}🍩 Ops! Esse sabor não existe no cardápio!{Style.RESET_ALL}")
