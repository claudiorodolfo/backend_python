import { useEffect, useState } from "react";
import { apiFetch } from "../api/client.js";

const empty = { nome: "", email: "" };

export default function PessoaForm({ editing, onSaved }) {
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
        await apiFetch(`/pessoas/${editing.id}`, {
          method: "PUT",
          body: values,
        });
      } else {
        await apiFetch("/pessoas", { method: "POST", body: values });
      }
      onSaved?.();
      setValues(empty);
    } catch (err) {
      setError(err.message ?? String(err));
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <form onSubmit={onSubmit} className="card">
      <div className="row" style={{ justifyContent: "space-between", marginBottom: "0.5rem" }}>
        <h2 style={{ fontSize: "1.05rem", margin: 0 }}>
          {editing ? "Editar pessoa" : "Nova pessoa"}
        </h2>
      </div>

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
