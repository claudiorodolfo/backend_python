## Aula 04 — State, Eventos e Renderização

### Objetivos

- Usar `useState`
- Entender estado como fonte de verdade
- Manipular eventos e atualizar UI

### `useState`

- Inicializa estado
- Retorna `[valor, setValor]`
- Alterar state dispara re-render

### Boas práticas

- Atualização baseada no valor anterior:
  - `setCount((c) => c + 1)`
- Estado complexo:
  - prefira objetos pequenos ou `useReducer` quando crescer

### Exercícios

1. Faça um formulário simples com:
   - input de `nome`
   - botão “Salvar”
   - ao salvar, mostre o nome salvo abaixo
2. Faça uma lista de tarefas em memória:
   - input + botão “Adicionar”
   - renderize lista

### Desafio

Faça um “filtro” de lista:

- Input `query`
- Renderize apenas itens que contém `query`

