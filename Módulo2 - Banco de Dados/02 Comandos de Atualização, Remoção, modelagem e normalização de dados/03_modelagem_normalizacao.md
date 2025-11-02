# 03 - Modelagem e Normalização de Dados

Este documento apresenta conceitos detalhados de modelagem de dados e normalização.

## 📊 Modelagem de Dados

### O que é Modelagem de Dados?

**Modelagem de dados** é o processo de criar uma representação abstrata dos dados que serão armazenados em um banco de dados. É uma fase crucial do desenvolvimento que ajuda a organizar e estruturar os dados de forma eficiente.

### Por que Modelar?

- ✅ **Organização**: Estrutura clara e lógica
- ✅ **Integridade**: Garante consistência dos dados
- ✅ **Performance**: Estrutura otimizada para consultas
- ✅ **Manutenibilidade**: Fácil de entender e modificar
- ✅ **Escalabilidade**: Preparado para crescimento

### Fases da Modelagem

#### 1. Modelagem Conceitual

**Objetivo**: Entender o problema e identificar entidades e relacionamentos.

**Atividades**:
- Identificar **entidades** (coisas do mundo real)
- Identificar **atributos** (características das entidades)
- Identificar **relacionamentos** (como entidades se conectam)
- Criar **Diagrama Entidade-Relacionamento (ER)**

**Exemplo - Sistema de Biblioteca:**
```
Entidades:
- Livro (título, autor, ISBN, ano)
- Usuário (nome, email, telefone)
- Empréstimo (data_emprestimo, data_devolucao)

Relacionamentos:
- Usuário faz Empréstimo (1:N)
- Livro está em Empréstimo (1:N)
```

#### 2. Modelagem Lógica

**Objetivo**: Converter o modelo conceitual em estrutura de tabelas.

**Atividades**:
- Converter entidades em tabelas
- Converter atributos em colunas
- Definir tipos de dados
- Definir chaves primárias
- Definir chaves estrangeiras
- Aplicar normalização

**Exemplo:**
```sql
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE livros (
    id INTEGER PRIMARY KEY,
    titulo VARCHAR(200),
    autor VARCHAR(100),
    isbn VARCHAR(20) UNIQUE
);

CREATE TABLE emprestimos (
    id INTEGER PRIMARY KEY,
    usuario_id INTEGER,
    livro_id INTEGER,
    data_emprestimo DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (livro_id) REFERENCES livros(id)
);
```

#### 3. Modelagem Física

**Objetivo**: Implementar o modelo no SGBD específico.

**Atividades**:
- Criar tabelas no banco de dados
- Criar índices para performance
- Definir constraints específicas do SGBD
- Otimizações baseadas no uso

### Princípios de Boa Modelagem

#### 1. Atomicidade

Cada campo deve representar um único valor atômico (indivisível).

**❌ Ruim:**
```
nome_completo: "João Silva Santos"
```

**✅ Bom:**
```
nome: "João"
sobrenome: "Silva Santos"
```

#### 2. Clareza nos Nomes

Use nomes descritivos e consistentes.

**❌ Ruim:**
```
tb1, col1, data1
```

**✅ Bom:**
```
clientes, nome, data_cadastro
```

#### 3. Consistência

Mantenha padrões consistentes.

- Prefixos de tabela (ou não usar)
- Nomenclatura (snake_case, camelCase)
- Tipos de dados similares para dados similares

#### 4. Integridade Referencial

Use chaves estrangeiras para manter relacionamentos válidos.

#### 5. Performance vs Normalização

Balance entre normalização completa e performance de consultas.

---

## 🔄 Normalização de Dados

### O que é Normalização?

**Normalização** é o processo de organizar dados em tabelas para:
- Eliminar **redundâncias**
- Prevenir **inconsistências**
- Melhorar **integridade**
- Facilitar **manutenção**

### Por que Normalizar?

**Problemas sem normalização:**
- ❌ Dados duplicados ocupam espaço desnecessário
- ❌ Atualizações precisam ser feitas em múltiplos lugares
- ❌ Risco de inconsistências (dados diferentes em lugares diferentes)
- ❌ Dificuldade de manutenção

**Benefícios da normalização:**
- ✅ Dados atualizados em um único lugar
- ✅ Menos espaço ocupado
- ✅ Mais consistência
- ✅ Facilita manutenção

### Formas Normais

#### 1ª Forma Normal (1FN)

**Regra**: Cada coluna deve conter apenas valores atômicos (indivisíveis). Não pode haver:
- Listas de valores em uma coluna
- Múltiplos valores separados por vírgula
- Arrays ou estruturas complexas

**❌ Exemplo NÃO Normalizado:**
```
┌────┬─────────┬────────────────────────┐
│ id │ nome    │ telefones              │
├────┼─────────┼────────────────────────┤
│ 1  │ João    │ (11) 9999-1111,        │
│    │         │ (11) 8888-2222         │
└────┴─────────┴────────────────────────┘
```

**Problemas:**
- Difícil de consultar telefones específicos
- Difícil de adicionar/remover telefones
- Não é possível indexar telefones

**✅ Exemplo Normalizado (Opção 1 - Tabela):**
```
┌────┬─────────┐  ┌────┬─────────────┬──────────────┐
│ id │ nome    │  │ id │ cliente_id  │ telefone     │
├────┼─────────┤  ├────┼─────────────┼──────────────┤
│ 1  │ João    │  │ 1  │ 1           │ (11) 9999-1111│
└────┴─────────┘  │ 2  │ 1           │ (11) 8888-2222│
                  └────┴─────────────┴──────────────┘
```

**✅ Exemplo Normalizado (Opção 2 - Múltiplas Linhas):**
```
┌────┬─────────┬──────────────┐
│ id │ nome    │ telefone     │
├────┼─────────┼──────────────┤
│ 1  │ João    │ (11) 9999-1111│
│ 1  │ João    │ (11) 8888-2222│
└────┴─────────┴──────────────┘
```

**Como aplicar 1FN:**
1. Identificar colunas com múltiplos valores
2. Criar tabelas separadas ou linhas múltiplas
3. Usar chave primária composta se necessário

#### 2ª Forma Normal (2FN)

**Regra**: Deve estar em 1FN e todos os atributos não-chave devem depender **completamente** da chave primária.

**Aplica-se quando:**
- A chave primária é **composta** (múltiplas colunas)
- Algum atributo depende apenas de parte da chave

**❌ Exemplo NÃO Normalizado:**
```
┌──────────┬──────────┬──────────┬──────────────┐
│ pedido_id│ produto_id│ produto  │ preco_unitario│
├──────────┼──────────┼──────────┼──────────────┤
│ 1        │ 1        │ Notebook │ 2999.99      │
│ 1        │ 2        │ Mouse    │ 49.90        │
│ 2        │ 1        │ Notebook │ 2999.99      │
└──────────┴──────────┴──────────┴──────────────┘

Chave primária: (pedido_id, produto_id)
Problema: produto e preco_unitario dependem apenas de produto_id!
```

**✅ Exemplo Normalizado:**
```
┌──────────┬──────────┬──────────┐  ┌──────────┬──────────┬──────────────┐
│ pedido_id│ produto_id│ quantidade│  │ produto_id│ nome    │ preco        │
├──────────┼──────────┼──────────┤  ├──────────┼──────────┼──────────────┤
│ 1        │ 1        │ 2        │  │ 1        │ Notebook │ 2999.99      │
│ 1        │ 2        │ 5        │  │ 2        │ Mouse    │ 49.90        │
│ 2        │ 1        │ 1        │  └──────────┴──────────┴──────────────┘
└──────────┴──────────┴──────────┘
```

**Como aplicar 2FN:**
1. Identificar chave primária composta
2. Verificar se há atributos que dependem apenas de parte da chave
3. Mover esses atributos para uma tabela separada

#### 3ª Forma Normal (3FN)

**Regra**: Deve estar em 2FN e não pode haver **dependência transitiva** (atributos não-chave dependendo de outros atributos não-chave).

**❌ Exemplo NÃO Normalizado:**
```
┌────┬──────────┬─────────┬─────────────┐
│ id │ produto  │ cidade  │ estado     │
├────┼──────────┼─────────┼─────────────┤
│ 1  │ Notebook │ SP      │ São Paulo  │
│ 2  │ Mouse    │ RJ      │ Rio        │
└────┴──────────┴─────────┴─────────────┘

Problema: estado depende de cidade, não de id!
```

**✅ Exemplo Normalizado:**
```
┌────┬──────────┬─────────┐  ┌─────────┬─────────────┐
│ id │ produto  │ cidade_id│  │ cidade_id│ cidade   │ estado     │
├────┼──────────┼─────────┤  ├─────────┼─────────────┤
│ 1  │ Notebook │ 1       │  │ 1       │ SP         │ São Paulo  │
│ 2  │ Mouse    │ 2       │  │ 2       │ RJ         │ Rio        │
└────┴──────────┴─────────┘  └─────────┴─────────────┘
```

**Como aplicar 3FN:**
1. Identificar dependências transitivas
2. Mover atributos dependentes para tabelas separadas
3. Criar chave estrangeira para manter relacionamento

### Formas Normais Avançadas

Existem outras formas normais (BCNF, 4FN, 5FN), mas para a maioria dos casos, a 3FN é suficiente.

### Quando Desnormalizar?

Às vezes, uma desnormalização controlada pode melhorar performance:

**Exemplo - Cache de dados calculados:**
```
-- Em vez de calcular sempre:
SELECT SUM(valor) FROM itens_pedido WHERE pedido_id = 1;

-- Pode desnormalizar:
ALTER TABLE pedidos ADD COLUMN valor_total DECIMAL(10,2);
```

**Quando fazer:**
- Consultas muito frequentes que são lentas
- Dados que raramente mudam
- Performance crítica

**Cuidados:**
- Manter dados sincronizados
- Documentar a desnormalização
- Usar triggers ou aplicação para manter consistência

---

## 📐 Exemplo Prático: Sistema de E-commerce

### Problema

Criar um sistema de e-commerce com:
- Clientes fazem pedidos
- Pedidos contêm produtos
- Produtos têm categorias
- Clientes têm endereços

### Passo 1: Modelagem Conceitual

**Entidades:**
- Cliente (nome, email, telefone)
- Endereço (rua, cidade, estado, CEP)
- Pedido (data, status, valor_total)
- Produto (nome, preco, descricao)
- Categoria (nome, descricao)
- ItemPedido (quantidade, preco_unitario, subtotal)

**Relacionamentos:**
- Cliente tem Endereços (1:N)
- Cliente faz Pedidos (1:N)
- Pedido contém ItensPedido (1:N)
- Produto está em ItensPedido (1:N)
- Produto pertence a Categoria (N:1)

### Passo 2: Modelagem Lógica (Normalizada)

```sql
-- Categorias
CREATE TABLE categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50) NOT NULL UNIQUE,
    descricao TEXT
);

-- Produtos
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    descricao TEXT,
    categoria_id INTEGER,
    estoque INTEGER DEFAULT 0,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

-- Clientes
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefone VARCHAR(20),
    data_cadastro DATE DEFAULT CURRENT_DATE
);

-- Endereços (1:N com clientes)
CREATE TABLE enderecos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    rua VARCHAR(200) NOT NULL,
    numero VARCHAR(10),
    complemento VARCHAR(100),
    cidade VARCHAR(50) NOT NULL,
    estado VARCHAR(2) NOT NULL,
    cep VARCHAR(10),
    tipo VARCHAR(20) DEFAULT 'residencial', -- residencial, comercial
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- Pedidos
CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    endereco_id INTEGER NOT NULL,
    data_pedido DATE DEFAULT CURRENT_DATE,
    status VARCHAR(20) DEFAULT 'pendente',
    valor_total DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (endereco_id) REFERENCES enderecos(id)
);

-- Itens do Pedido
CREATE TABLE itens_pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK(quantidade > 0),
    preco_unitario DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);
```

### Análise de Normalização

**1FN**: ✅ Cada campo tem valores atômicos

**2FN**: ✅ Não há chave primária composta (exceto itens_pedido, mas está correta)

**3FN**: ✅ Não há dependências transitivas
- `endereco.estado` não depende de `pedido.id`, depende de `endereco.cidade` - mas está em tabela separada

### Benefícios desta Estrutura

- ✅ **Integridade**: Atualizar email do cliente em um lugar só
- ✅ **Consistência**: Preços de produtos não se repetem em cada pedido
- ✅ **Manutenibilidade**: Fácil de entender e modificar
- ✅ **Escalabilidade**: Preparado para crescimento

---

## ⚖️ Balanceamento: Normalização vs Performance

### Trade-offs

**Normalização Excessiva:**
- ❌ Muitos JOINs em consultas
- ❌ Consultas mais lentas
- ❌ Maior complexidade

**Desnormalização Excessiva:**
- ❌ Dados duplicados
- ❌ Inconsistências
- ❌ Mais espaço

### Estratégia Recomendada

1. **Comece Normalizado**: Modelo em 3FN
2. **Meça Performance**: Identifique consultas lentas
3. **Desnormalize Seletivamente**: Apenas onde necessário
4. **Documente**: Mantenha registro das desnormalizações

### Exemplos de Desnormalização Controlada

#### 1. Cache de Soma
```sql
-- Em vez de calcular sempre:
SELECT SUM(subtotal) FROM itens_pedido WHERE pedido_id = 1;

-- Desnormalizar:
ALTER TABLE pedidos ADD COLUMN valor_total DECIMAL(10,2);

-- Atualizar via trigger ou aplicação
```

#### 2. Dados Frequentemente Consultados Juntos
```sql
-- Se sempre consulta nome do cliente com pedido:
ALTER TABLE pedidos ADD COLUMN cliente_nome VARCHAR(100);

-- Atualizar quando cliente mudar nome (via trigger)
```

---

## ✅ Checklist de Modelagem

Antes de finalizar seu modelo, verifique:

- [ ] Todas as tabelas estão em pelo menos 3FN?
- [ ] Todas as chaves primárias estão definidas?
- [ ] Todas as chaves estrangeiras estão definidas?
- [ ] Nomes são claros e descritivos?
- [ ] Tipos de dados são apropriados?
- [ ] Há índices nas colunas frequentemente consultadas?
- [ ] Constraints (NOT NULL, UNIQUE, CHECK) estão definidas?
- [ ] O modelo está documentado?

---

## 📝 Resumo

**Modelagem de Dados:**
- Processo em 3 fases: Conceitual → Lógica → Física
- Foco em organização, integridade e performance

**Normalização:**
- 1FN: Valores atômicos
- 2FN: Dependência completa da chave
- 3FN: Sem dependências transitivas
- Balancear com performance

**Boas Práticas:**
- Começar normalizado
- Medir performance
- Desnormalizar seletivamente
- Documentar decisões

Boa modelagem leva a bons bancos de dados! 🎯

