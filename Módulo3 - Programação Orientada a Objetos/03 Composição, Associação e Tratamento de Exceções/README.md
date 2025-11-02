# Composição, Associação e Tratamento de Exceções

Este material aborda relacionamentos entre classes (composição e associação) e o tratamento de exceções em contexto orientado a objetos, essenciais para criar sistemas robustos e resilientes.

## 📚 Conteúdo

1. [Composição](#composição)
2. [Associação](#associação)
3. [Diferença entre Composição e Associação](#diferença-entre-composição-e-associação)
4. [Exemplos Práticos de Associação](#exemplos-práticos-de-associação)
5. [Exceções Customizadas](#exceções-customizadas)
6. [Tratamento com try-except em Classes](#tratamento-com-try-except-em-classes)

---

## Composição

**Composição** é um relacionamento forte onde uma classe **contém** outra classe como parte essencial. O objeto composto **não pode existir** sem o componente.

### Características:

- ✅ **Relacionamento "TEM-UM" forte**: O objeto composto possui o componente
- ✅ **Dependência forte**: O componente não existe independentemente
- ✅ **Ciclo de vida compartilhado**: Quando o objeto composto é destruído, o componente também é

### Exemplo:

```python
class Motor:
    pass

class Carro:
    def __init__(self):
        self.motor = Motor()  # Composição: Carro TEM-UM Motor
```

O carro **possui** um motor como parte essencial. Sem motor, não há carro.

---

## Associação

**Associação** é um relacionamento fraco onde uma classe **usa** outra classe, mas não possui necessariamente. O objeto associado **pode existir independentemente**.

### Características:

- ✅ **Relacionamento "USA"**: Uma classe usa outra, mas não possui
- ✅ **Dependência fraca**: Os objetos podem existir independentemente
- ✅ **Ciclo de vida independente**: Objetos não compartilham ciclo de vida

### Tipos de Associação:

1. **Associação Simples**: Uma classe referencia outra
2. **Agregação**: Relacionamento "TEM-UM" fraco (o agregado pode existir sem)
3. **Composição**: Relacionamento "TEM-UM" forte (não pode existir sem)

### Exemplo:

```python
class Pessoa:
    pass

class Biblioteca:
    def __init__(self):
        self.visitantes = []  # Associação: Biblioteca tem lista de pessoas
    
    def adicionar_visitante(self, pessoa):
        self.visitantes.append(pessoa)  # Pessoa pode existir sem biblioteca
```

---

## Diferença entre Composição e Associação

| Aspecto | Composição | Associação |
|---------|-------------|------------|
| **Força** | Forte | Fraca |
| **Existência** | Componente não existe sem composto | Objeto pode existir independentemente |
| **Ciclo de vida** | Compartilhado | Independente |
| **Propriedade** | "Possui" fortemente | "Usa" ou "Referencia" |
| **Exemplo** | Carro TEM Motor | Biblioteca TEM lista de Pessoas |

### Regra Prática:

- **Composição**: Se o objeto **não faz sentido sem** o componente → Composição
- **Associação**: Se o objeto **pode existir sem** o outro → Associação

---

## Exemplos Práticos de Associação

### 1. Associação Um-para-Muitos

```python
class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []  # Um professor tem muitos alunos

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.professor = None  # Um aluno tem um professor
```

### 2. Associação Muitos-para-Muitos

```python
class Estudante:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []  # Um estudante tem muitos cursos

class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.estudantes = []  # Um curso tem muitos estudantes
```

---

## Exceções Customizadas

Criar **exceções customizadas** permite definir erros específicos do seu domínio, tornando o código mais claro e facilitando o tratamento de erros.

### Por que criar exceções customizadas?

- ✅ **Clareza**: Erros mais específicos e descritivos
- ✅ **Controle**: Tratar diferentes tipos de erro de formas diferentes
- ✅ **Depuração**: Mais fácil identificar a origem do problema
- ✅ **Documentação**: Indica claramente quais erros podem ocorrer

### Como criar:

```python
class MinhaExcecao(Exception):
    """Exceção customizada."""
    pass

# Com mensagem
class ValorInvalidoError(Exception):
    """Exceção para valores inválidos."""
    def __init__(self, mensagem, valor):
        self.mensagem = mensagem
        self.valor = valor
        super().__init__(f"{mensagem}: {valor}")
```

---

## Tratamento com try-except em Classes

Tratar exceções **dentro de classes** permite:
- Validar dados nos métodos
- Lançar exceções apropriadas
- Tratar erros de forma elegante
- Manter o estado consistente

### Padrões comuns:

1. **Validação em métodos**: Validar e lançar exceções
2. **Try-except em métodos**: Tratar erros e manter consistência
3. **Exceções customizadas**: Criar tipos específicos de erro
4. **Propagação controlada**: Decidir quando tratar e quando propagar

---

## 📁 Arquivos de Exemplo

Este diretório contém exemplos práticos:

1. **01_composicao.py** - Relacionamento de composição
2. **02_associacao.py** - Relacionamento de associação
3. **03_diferenca_composicao_associacao.py** - Comparação prática
4. **04_exemplos_associacao.py** - Exemplos de associação
5. **05_excecoes_customizadas.py** - Criando exceções personalizadas
6. **06_try_except_classes.py** - Tratamento de exceções em classes
7. **07_validacao_classes.py** - Validação com exceções
8. **08_exemplo_completo.py** - Sistema completo integrando todos os conceitos

Execute cada arquivo para ver os exemplos em ação:

```bash
python3 01_composicao.py
python3 02_associacao.py
# ... e assim por diante
```

---

## 🎯 Próximos Passos

Após dominar composição, associação e tratamento de exceções, você terá:
- ✅ Conhecimento completo dos relacionamentos entre classes
- ✅ Capacidade de criar sistemas robustos com tratamento de erros
- ✅ Habilidade para modelar relacionamentos complexos

---

## 💡 Dicas

1. **Use Composição quando**: O objeto não faz sentido sem o componente
2. **Use Associação quando**: Objetos podem existir independentemente
3. **Crie exceções customizadas**: Para erros específicos do seu domínio
4. **Trate exceções apropriadamente**: Não ignore erros, mas trate de forma elegante
5. **Valide em métodos**: Use exceções para validar dados de entrada
6. **Documente exceções**: Indique quais exceções cada método pode lançar
7. **Mantenha estado consistente**: Use try-except para garantir consistência

