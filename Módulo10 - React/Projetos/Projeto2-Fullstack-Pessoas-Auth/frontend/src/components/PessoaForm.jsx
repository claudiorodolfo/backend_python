import { useEffect, useState } from "react";
import { apiFetch } from "../api/client.js";
import { useAuth } from "../context/AuthContext.jsx";

const empty = { nome: "", email: "" };

export default function PessoaForm({ editing, onSaved }) {
  const { token, logout } = useAuth();
  const [values, setValues] = useState(empty);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    if (editing) {
      setValues({ nome: editing.nome, email: editing.email });
    } else {
      setValues(empty);
    }
  }, [editing]);

  async function onSubmit(e) {
    e.preventDefault();
    setError("");
    setSubmitting(true);
    try {
      if (editing) {
        await apiFetch(`/pessoas/${editing.id}`, { method: "PUT", body: values, token });
      } else {
        await apiFetch("/pessoas", { method: "POST", body: values, token });
      }
      onSaved?.();
      setValues(empty);
    } catch (err) {
      if (String(err.message).includes("Token") || String(err.message).includes("Credenciais")) {
        logout();
      }
      setError(err.message ?? String(err));
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <form onSubmit={onSubmit} className="card">
      <h2 style={{ fontSize: "1.05rem", margin: "0 0 0.75rem" }}>
        {editing ? "Editar pessoa" : "Nova pessoa"}
      </h2>

      <label>
        Nome
        <input
          value={values.nome}
          onChange={(e) => setValues((v) => ({ ...v, nome: e.target.value }))}
          required
        />
      </label>

      <label>
        E-mail
        <input
          type="email"
          value={values.email}
          onChange={(e) => setValues((v) => ({ ...v, email: e.target.value }))}
          required
        />
      </label>

      {error ? <p className="error">{error}</p> : null}

      <button type="submit" disabled={submitting}>
        {submitting ? "Salvando…" : "Salvar"}
      </button>
    </form>
  );
}
