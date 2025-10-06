# 🍩 TO-DONUT Terminal
**Suas tarefas nunca foram tão doces!**

<div align="center">

```
════════════════════════════════════════════════════════════
   🍩  TO-DONUT  🍩  Suas tarefas nunca foram tão doces!  🍩
════════════════════════════════════════════════════════════
```

*Um gerenciador de tarefas de terminal colorido e delicioso!*

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Colorama](https://img.shields.io/badge/Colorama-0.4.6-pink.svg)](https://pypi.org/project/colorama/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with Love](https://img.shields.io/badge/Made%20with-❤️%20%26%20🍩-pink.svg)](https://github.com/igorland1/to-donut-terminal)

</div>

## 🎯 O que é o TO-DONUT?

TO-DONUT é um gerenciador de tarefas para terminal totalmente personalizado com tema de donuts! Transforme sua rotina de produtividade em uma experiência visual colorida e divertida. Cada tarefa é um donut esperando para ser criado, saboreado e devorado!

### 🌟 Por que "TO-DONUT"?

- **TO-DO** + **DONUT** = Produtividade deliciosa!
- Cada tarefa é um donut em sua caixa pessoal
- Interface colorida que torna o trabalho mais divertido
- Frases motivacionais aleatórias com tema de confeitaria
- Porque produtividade pode (e deve!) ser doce

## ✨ Funcionalidades

### 🎨 Interface Ultra Colorida
Usando a biblioteca **Colorama**, o TO-DONUT traz:
- **Banner de boas-vindas** animado ao iniciar
- **Cores vibrantes temáticas:**
  - 🌸 Rosa/Magenta para menus e banners
  - 🍯 Caramelo/Amarelo para ações de adicionar
  - 🍓 Morango/Vermelho claro para avisos
  - 🍦 Baunilha/Ciano para listagens
  - ✅ Verde para tarefas concluídas
  - 🎨 Branco polvilhado para destaques

### 🍩 Menu da Doceria
| Opção | Ação | Descrição |
|-------|------|-----------|
| **[1] 🍩 Adicionar Donut** | Criar tarefa | "Que sabor de donut você quer criar?" |
| **[2] 🍩 Ver Caixa de Donuts** | Listar tarefas | Visualize sua caixa de donuts |
| **[3] 🍩 Mudar Sabor** | Atualizar | "Donut reformulado! Nova receita!" |
| **[4] 🍩 Devorar Donut** | Concluir | "Nhac! Donut devorado com sucesso!" |
| **[5] 🍩 Limpar Migalhas** | Remover concluídas | Limpa donuts já saboreados |
| **[6] 🍩 Fechar Doceria** | Sair | Despedida doce e colorida |

### 🎯 Estados Visuais das Tarefas
- 🍩 **Donut Fresco** (Amarelo) - Tarefa pendente esperando
- 🍩✨ **Donut Saboreado** (Verde) - Tarefa concluída com brilho!

### 💬 Frases de Efeito Aleatórias

Cada ação exibe uma frase motivacional aleatória:

**Ao adicionar tarefa:**
- "🍩 Mmm... Tarefa fresquinha saindo do forno!"
- "🍩 Que delícia! Mais uma tarefa na bandeja!"
- "🍩 Sua lista tá crescendo como massa de donut!"
- "🍩 Polvilhada e pronta! Tarefa adicionada!"

**Ao concluir tarefa:**
- "🍩✨ Nhac! Donut devorado com sucesso!"
- "🍩✨ Que sabor maravilhoso! Tarefa concluída!"
- "🍩✨ Delicioso! Mais um donut saboreado!"
- "🍩✨ Mmm... Esse tava uma delícia! Concluído!"

**Mensagens especiais:**
- Caixa vazia: "🍩 Sua caixa de donuts está vazia! Hora de adicionar tarefas!"
- Donut reformulado: "🍩 Donut reformulado! Nova receita aplicada!"
- Limpando migalhas: "🍩 Limpando as migalhas... X donut(s) removido(s)!"

## 🚀 Como usar

### Pré-requisitos
- Python 3.7 ou superior
- Terminal que suporte cores ANSI (Windows, Linux, macOS)
- Biblioteca Colorama

### Instalação

```bash
# Clone o repositório
git clone https://github.com/igorland1/to-donut-terminal.git

# Entre na pasta
cd to-donut-terminal

# Instale as dependências
pip install -r requirements.txt

# Execute o programa
python gerenciador.py
```

### Instalação rápida
```bash
pip install colorama
python gerenciador.py
```

### Primeiro uso
1. Execute `python gerenciador.py`
2. Veja o banner colorido da TO-DONUT aparecer! 🍩
3. Escolha **[1]** para adicionar seu primeiro donut (tarefa)
4. Use **[2]** para ver sua caixa de donuts
5. **[4]** para devorar um donut quando concluir a tarefa!
6. **[5]** para limpar as migalhas (remover concluídas)

## 📸 Preview do Terminal

```
════════════════════════════════════════════════════════════
   🍩  TO-DONUT  🍩  Suas tarefas nunca foram tão doces!  🍩
════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════╗
║        🍩  MENU DA DOCERIA TO-DONUT  🍩                  ║
╚══════════════════════════════════════════════════════════╝

[1]🍩 Adicionar Donut (Nova Tarefa)
[2]🍩 Ver Caixa de Donuts (Listar Tarefas)
[3]🍩 Mudar Sabor (Atualizar Tarefa)
[4]🍩 Devorar Donut (Concluir Tarefa)
[5]🍩 Limpar Migalhas (Remover Concluídas)
[6]🍩 Fechar a Doceria (Sair)

🍩 Escolha seu donut: 2

────────────────────────────────────────────────────────────
   🍩  SUA CAIXA DE DONUTS (Tarefas)  🍩
────────────────────────────────────────────────────────────

🍩 1. [ ] Estudar Python
🍩✨ 2. [✓] Fazer exercícios
🍩 3. [ ] Criar projeto terminal
🍩✨ 4. [✓] Personalizar to-donut
```

> **Nota:** As cores não aparecem aqui, mas no terminal você verá:
> - Menu em rosa/magenta vibrante
> - Tarefas pendentes em amarelo
> - Tarefas concluídas em verde brilhante
> - Mensagens especiais em cores temáticas!

## 🎨 Personalização Aplicada

### 🌈 Sistema de Cores Colorama
O projeto utiliza a biblioteca **Colorama** para cores multiplataforma:

```python
# Cores tema donut definidas
ROSA_DONUT = Fore.LIGHTMAGENTA_EX    # Banners e menus principais
CHOCOLATE = Fore.YELLOW              # Tarefas pendentes
MORANGO = Fore.LIGHTRED_EX           # Avisos e mensagens especiais
BAUNILHA = Fore.LIGHTCYAN_EX         # Listagens e informações
POLVILHO = Fore.LIGHTWHITE_EX        # Destaques e inputs
CARAMELO = Fore.LIGHTYELLOW_EX       # Ações de adicionar
Verde = Fore.GREEN                    # Tarefas concluídas
```

### 📝 Modificações Implementadas

#### ✅ **1. Sistema de Cores Completo**
- Importação e inicialização do Colorama
- Paleta de 6 cores temáticas de donuts
- Cada ação tem sua cor específica
- Auto-reset de cores após cada uso

#### ✅ **2. Banner de Boas-vindas**
- Função `banner()` com arte ASCII
- Exibido automaticamente ao iniciar
- Bordas decorativas coloridas

#### ✅ **3. Frases Aleatórias Motivacionais**
- Sistema com `random.choice()` em cada ação
- 4 variações para adicionar tarefas
- 4 variações para concluir tarefas
- Mensagens contextuais personalizadas

#### ✅ **4. Menu Redesenhado**
- Bordas Unicode estilizadas (╔═╗║╚╝)
- Cada opção com emoji e cor própria
- Descrições criativas com tema de donut

#### ✅ **5. Visualização de Tarefas**
- Título decorativo com separadores
- Emoji diferente para pendente (🍩) e concluído (🍩✨)
- Cores distintas por estado
- Mensagem especial para lista vazia

#### ✅ **6. Inputs Personalizados**
- Prompts coloridos e temáticos
- Perguntas criativas: "Que sabor de donut você quer criar?"
- Feedback visual imediato

#### ✅ **7. Mensagem de Despedida**
- Banner especial ao sair
- Agradecimento temático
- Formatação colorida

### 🔧 Como Personalizar Ainda Mais

**Adicionar novas frases:**
```python
# Em adicionar_tarefa(), linha 23-28
frases = [
    "🍩 Sua nova frase aqui!",
    # ... adicione mais
]
```

**Mudar cores:**
```python
# No topo do arquivo, linhas 8-13
ROSA_DONUT = Fore.LIGHTBLUE_EX  # Mude para azul claro
```

## 🛠️ Roadmap Futuro

### 🍫 Ideias para evolução
- [ ] Persistência de dados (JSON/SQLite)
- [ ] Prioridades por sabor (Chocolate=urgente, Baunilha=normal)
- [ ] Contador de donuts saboreados
- [ ] Sistema de conquistas
- [ ] Exportar lista para arquivo
- [ ] Modo "Dark Chocolate" (tema escuro)
- [ ] Integração com notificações do sistema

## 🤝 Contribuindo

Quer tornar o TO-DONUT ainda mais doce? Contribuições são muito bem-vindas!

1. **Fork** o projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. **Commit** suas mudanças (`git commit -m 'feat: adiciona nova funcionalidade doce'`)
4. **Push** para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um **Pull Request**

### 💡 Ideias para contribuir
- 🎨 Novos temas de cores
- 💬 Mais frases motivacionais criativas
- ✨ Novos emojis e animações
- 🍫 Sistema de prioridades por sabores
- 💾 Persistência de dados
- 🐛 Correção de bugs

## 🐛 Encontrou um bug?

Abra uma **issue** detalhando:
1. O que você estava fazendo
2. O que aconteceu (comportamento atual)
3. O que você esperava (comportamento esperado)
4. Capturas de tela ou logs (se possível)
5. Seu sistema operacional e versão do Python

## 📦 Dependências

```txt
colorama>=0.4.6  # Para cores multiplataforma no terminal
```

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🎉 Changelog

### v2.0.0 - Personalização Donut Completa
- ✅ Adicionado sistema completo de cores com Colorama
- ✅ Implementado banner de boas-vindas colorido
- ✅ Criadas frases motivacionais aleatórias
- ✅ Redesenhado menu com bordas Unicode e emojis
- ✅ Personalizado todos os inputs e outputs
- ✅ Adicionado emoji especial para tarefas concluídas (✨)
- ✅ Criada mensagem de despedida temática
- ✅ Melhorada experiência visual geral

### v1.0.0 - Versão Inicial
- Sistema básico de gerenciamento de tarefas
- Funcionalidades CRUD completas

## ❤️ Agradecimentos

- 🙏 Inspirado na necessidade de tornar a produtividade mais divertida
- 💻 Para todos que acreditam que código pode ser funcional **E** bonito
- 🍩 E claro, para os donuts que nos inspiram e adoçam nossos dias!
- 🎨 Agradecimento especial à biblioteca Colorama

---

<div align="center">

**Feito com ❤️ e muitos 🍩 por [Igor Landi](https://github.com/igorland1)**

*"A vida é como um donut - melhor quando é doce, colorida e compartilhada!"*

⭐ **Se você gostou, deixe uma estrela no GitHub!** ⭐

[![GitHub stars](https://img.shields.io/github/stars/igorland1/to-donut-terminal?style=social)](https://github.com/igorland1/to-donut-terminal)
[![GitHub forks](https://img.shields.io/github/forks/igorland1/to-donut-terminal?style=social)](https://github.com/igorland1/to-donut-terminal/fork)

</div>
