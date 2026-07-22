## Aula 02 — React: o que é e como pensar

### Objetivos

- Entender React como **UI declarativa**
- Saber o que é **componente** e **estado**
- Aprender o fluxo: **dados descem (props)** e **eventos sobem (callbacks)**

### Modelo mental

- Você descreve **como a UI deve parecer** para um determinado estado.
- Quando o estado muda, React recalcula o que precisa mudar na tela.

### Componentes

- **Funções** que retornam UI (JSX)
- Recebem **props** (entrada) e podem ter **state** (memória)

### Renderização e re-render

- Mudou state/props → componente renderiza de novo
- Render é barato; o importante é **evitar re-render desnecessário em cascata**

### Regras práticas

- Evite duplicar estado (derive quando puder)
- Estado deve morar “o mais alto possível”, mas “o mais baixo necessário”

### Exercícios

1. No seu app, crie 3 componentes:
   - `Header` (título)
   - `Main` (conteúdo)
   - `Footer` (rodapé)
2. Passe uma prop `appName` para `Header`

### Desafio

Faça um componente `Counter` com:

- Um número exibido
- Botões `+1` e `-1`

