# Abstract Factory Pattern - Sistema de Temas GUI

Este projeto demonstra a implementação do padrão **Abstract Factory** (Fábrica Abstrata) em Python, utilizando um exemplo prático de um sistema de temas de interface gráfica que cria famílias de componentes relacionados (botões e caixas de seleção) para diferentes temas visuais.

## 📋 Sobre o Padrão

O **Abstract Factory** é um padrão de projeto criacional que fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas. Este padrão é útil quando você precisa criar grupos de objetos que trabalham juntos e precisam ser consistentes entre si.

No contexto deste exemplo, o padrão garante que todos os componentes de interface (botões, caixas de seleção, etc.) sejam criados com o mesmo tema visual, mantendo a consistência da interface do usuário.

## 🏗️ Estrutura do Projeto

```
exemplo2/
├── main.py                  # Arquivo principal de demonstração
├── abstract_factory.py      # Interface da fábrica abstrata (FabricaGUI)
├── interfaces.py            # Interfaces abstratas dos produtos (Botao, CaixaSelecao)
├── factories.py             # Fábricas concretas (FabricaClara, FabricaEscura)
├── light_theme.py           # Produtos concretos para tema claro
└── dark_theme.py            # Produtos concretos para tema escuro
```

## 🎯 Componentes do Padrão

### 1. Abstract Factory (Fábrica Abstrata)
- **`FabricaGUI`**: Interface abstrata que define os métodos para criar componentes relacionados (botão e caixa de seleção)

### 2. Concrete Factories (Fábricas Concretas)
- **`FabricaClara`**: Cria componentes do tema claro (BotaoClaro + CaixaSelecaoClara)
- **`FabricaEscura`**: Cria componentes do tema escuro (BotaoEscuro + CaixaSelecaoEscura)

### 3. Abstract Products (Produtos Abstratos)
- **`Botao`**: Interface abstrata para componentes de botão
- **`CaixaSelecao`**: Interface abstrata para componentes de caixa de seleção

### 4. Concrete Products (Produtos Concretos)
- **`BotaoClaro`**: Implementação concreta de botão no tema claro
- **`BotaoEscuro`**: Implementação concreta de botão no tema escuro
- **`CaixaSelecaoClara`**: Implementação concreta de caixa de seleção no tema claro
- **`CaixaSelecaoEscura`**: Implementação concreta de caixa de seleção no tema escuro

## 🚀 Como Executar

1. Navegue até o diretório do projeto:
```bash
cd "Módulo4 - Padrões de Desenvolvimento de Software/Padrões Criacionais/abstract_factory/exemplo2"
```

2. Execute o arquivo principal:
```bash
python main.py
```

3. O programa irá demonstrar a criação de componentes para ambos os temas (claro e escuro).

## 💡 Exemplo de Uso

```python
from abstract_factory import FabricaGUI
from factories import FabricaClara, FabricaEscura

# Função que renderiza interface usando uma fábrica
def renderizarInterface(fabrica: FabricaGUI):
    botao = fabrica.criarBotao()
    caixaSelecao = fabrica.criarCaixaSelecao()
    print(botao.renderizar())
    print(caixaSelecao.renderizar())

# Usar tema claro
renderizarInterface(FabricaClara())
# Output:
# Botão claro
# Checkbox claro

# Usar tema escuro
renderizarInterface(FabricaEscura())
# Output:
# Botão escuro
# Checkbox escuro
```

## ✨ Benefícios do Padrão

1. **Consistência Visual**: Garante que todos os componentes de uma interface usem o mesmo tema
2. **Flexibilidade**: Facilita a troca de temas sem modificar o código cliente
3. **Desacoplamento**: O código cliente não depende de classes concretas de componentes
4. **Extensibilidade**: Novos temas podem ser adicionados criando novas fábricas e produtos sem modificar código existente
5. **Manutenibilidade**: Mudanças em um tema não afetam outros temas

## 🔄 Fluxo de Execução

1. O cliente solicita uma fábrica de um tema específico (claro ou escuro)
2. A fábrica correspondente é instanciada (`FabricaClara` ou `FabricaEscura`)
3. A fábrica cria os componentes relacionados (botão + caixa de seleção) do mesmo tema
4. Os componentes são utilizados através de suas interfaces abstratas
5. Todos os componentes garantem consistência visual entre si

## 📊 Diagrama de Classes (Conceitual)

```
FabricaGUI (Abstract Factory)
    ├── criarBotao() -> Botao
    └── criarCaixaSelecao() -> CaixaSelecao
            │
            ├── FabricaClara (Concrete Factory)
            │   ├── criarBotao() -> BotaoClaro
            │   └── criarCaixaSelecao() -> CaixaSelecaoClara
            │
            └── FabricaEscura (Concrete Factory)
                ├── criarBotao() -> BotaoEscuro
                └── criarCaixaSelecao() -> CaixaSelecaoEscura

Botao (Abstract Product)
    ├── BotaoClaro (Concrete Product)
    └── BotaoEscuro (Concrete Product)

CaixaSelecao (Abstract Product)
    ├── CaixaSelecaoClara (Concrete Product)
    └── CaixaSelecaoEscura (Concrete Product)
```

## 🔍 Diferenças entre Abstract Factory e Factory Method

- **Factory Method**: Cria um único tipo de produto
- **Abstract Factory**: Cria famílias de produtos relacionados

Neste exemplo, o Abstract Factory é usado porque precisamos garantir que botões e caixas de seleção sejam sempre do mesmo tema, criando uma família consistente de componentes.

## 🎨 Casos de Uso Reais

Este padrão é comumente usado em:
- Sistemas de temas de interface (como neste exemplo)
- Bibliotecas de UI multiplataforma (criar componentes nativos para cada plataforma)
- Sistemas de configuração de produtos relacionados
- Frameworks de jogos (criar famílias de objetos de jogo para diferentes estilos)

## 🛠️ Tecnologias

- **Python 3.x**
- **ABC (Abstract Base Classes)**: Para definir interfaces abstratas
- **Type Hints**: Para melhor documentação e verificação de tipos

## 📚 Referências

- Padrão de Projeto: Abstract Factory (Gang of Four - Design Patterns)
- [Python ABC Documentation](https://docs.python.org/3/library/abc.html)

## 🔄 Extensões Possíveis

Para expandir este exemplo, você poderia:

1. **Adicionar novos temas**: Criar `FabricaAzul`, `FabricaVerde`, etc.
2. **Adicionar novos componentes**: Criar interfaces para `CampoTexto`, `Menu`, etc.
3. **Implementar renderização real**: Usar bibliotecas como Tkinter ou PyQt para renderização visual
4. **Adicionar configurações**: Permitir personalização de cores, fontes, etc.

---

**Boa prática de aprendizado! 🚀**

