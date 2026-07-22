## Aula 06 — Formulários controlados e validação

### Objetivos

- Montar forms com inputs **controlados** (`value` + `onChange`)
- Enviar dados para o FastAPI (`POST`, `PUT`) em JSON
- Validar no cliente antes de chamar a API

### Form controlado

- O React é a fonte de verdade do que está digitado.
- No submit, monte o payload e chame a API.

```jsx
const [nome, setNome] = useState("");
const [email, setEmail] = useState("");

async function onSubmit(e) {
  e.preventDefault();
  await fetch(`${API}/pessoas`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nome, email }),
  });
}
```

### Alinhamento com FastAPI / Pydantic

Se o backend rejeitar o corpo (422), leia `detail` da resposta para mostrar erros úteis.

### Exercícios

1. Form de criação: `nome`, `email`, botão Salvar, limpar campos após sucesso.
2. Mostre erro se `email` não contiver `@`.
3. Desabilite o botão enquanto o `fetch` está em andamento (`isSubmitting`).

### Desafio

Implemente edição: um form que recebe `pessoa` inicial e usa `PUT /pessoas/{id}` (`Projeto1`).
