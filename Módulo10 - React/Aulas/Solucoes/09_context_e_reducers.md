# Soluções — Aula 09

## Exercício 1 — `ThemeProvider` e classe no `body`

```jsx
import {
  createContext,
  useContext,
  useEffect,
  useMemo,
  useState,
} from "react";

const ThemeCtx = createContext(null);

export function ThemeProvider({ children }) {
  const [tema, setTema] = useState("claro");

  useEffect(() => {
    document.body.classList.remove("tema-claro", "tema-escuro");
    document.body.classList.add(
      tema === "escuro" ? "tema-escuro" : "tema-claro"
    );
  }, [tema]);

  const value = useMemo(() => ({ tema, setTema }), [tema]);
  return <ThemeCtx.Provider value={value}>{children}</ThemeCtx.Provider>;
}

export function useTheme() {
  const ctx = useContext(ThemeCtx);
  if (!ctx) throw new Error("useTheme fora do ThemeProvider");
  return ctx;
}
```

## Exercício 2 — `AuthProvider` em memória

```jsx
import {
  createContext,
  useCallback,
  useContext,
  useMemo,
  useState,
} from "react";

const AuthCtx = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(null);

  const login = useCallback((u, t) => {
    setUser(u);
    setToken(t);
  }, []);

  const logout = useCallback(() => {
    setUser(null);
    setToken(null);
  }, []);

  const value = useMemo(
    () => ({ user, token, login, logout }),
    [user, token, login, logout]
  );

  return <AuthCtx.Provider value={value}>{children}</AuthCtx.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthCtx);
  if (!ctx) throw new Error("useAuth fora do AuthProvider");
  return ctx;
}
```

## Desafio — Formulário multi-etapas com `useReducer`

```jsx
import { useReducer } from "react";

const initial = { step: 0, nome: "", email: "", cidade: "" };

function reducer(state, action) {
  switch (action.type) {
    case "SET_FIELD":
      return { ...state, [action.field]: action.value };
    case "NEXT":
      return { ...state, step: Math.min(state.step + 1, 2) };
    case "BACK":
      return { ...state, step: Math.max(state.step - 1, 0) };
    case "RESET":
      return initial;
    default:
      return state;
  }
}

export default function WizardForm() {
  const [state, dispatch] = useReducer(reducer, initial);

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        console.log(state);
      }}
    >
      {state.step === 0 && (
        <input
          value={state.nome}
          onChange={(e) =>
            dispatch({ type: "SET_FIELD", field: "nome", value: e.target.value })
          }
          placeholder="Nome"
        />
      )}
      {state.step === 1 && (
        <input
          value={state.email}
          onChange={(e) =>
            dispatch({
              type: "SET_FIELD",
              field: "email",
              value: e.target.value,
            })
          }
          placeholder="E-mail"
        />
      )}
      {state.step === 2 && (
        <input
          value={state.cidade}
          onChange={(e) =>
            dispatch({
              type: "SET_FIELD",
              field: "cidade",
              value: e.target.value,
            })
          }
          placeholder="Cidade"
        />
      )}
      <div>
        {state.step > 0 ? (
          <button type="button" onClick={() => dispatch({ type: "BACK" })}>
            Voltar
          </button>
        ) : null}
        {state.step < 2 ? (
          <button type="button" onClick={() => dispatch({ type: "NEXT" })}>
            Próximo
          </button>
        ) : (
          <button type="submit">Enviar</button>
        )}
      </div>
    </form>
  );
}
```
