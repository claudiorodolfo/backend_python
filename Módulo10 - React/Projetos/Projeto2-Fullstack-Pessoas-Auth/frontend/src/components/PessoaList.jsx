import { useEffect, useState } from "react";
import { apiFetch } from "../api/client.js";
import { useAuth } from "../context/AuthContext.jsx";

export default function PessoaList({ refreshKey, onSelect, onChanged }) {
  const { token, logout } = useAuth();
  const [pessoas, setPessoas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let alive = true;

    async function load() {
      try {
        setLoading(true);
        setError("");
        const data = await apiFetch("/pessoas", { token });
        if (alive) setPessoas(data);
      } catch (e) {
        if (alive) setError(e.message ?? String(e));
      } finally {
        if (alive) setLoading(false);
      }
    }

    load();
    return () => {
      alive = false;
    };
  }, [refreshKey, token]);

  async function remover(id) {
    if (!confirm("Remover esta pessoa?")) return;
    try {
      await apiFetch(`/pessoas/${id}`, { method: "DELETE", token });
      onChanged?.();
    } catch (e) {
      if (String(e.message).includes("Token")) logout();
      alert(e.message ?? String(e));
    }
  }

  if (loading) return <p className="muted">Carregando pessoas…</p>;
  if (error) return <p className="error">Erro: {error}</p>;
  if (!pessoas.length) return <p className="muted">Nenhuma pessoa cadastrada.</p>;

  return (
    <ul style={{ listStyle: "none", padding: 0, margin: 0 }}>
      {pessoas.map((p) => (
        <li key={p.id} className="card row" style={{ justifyContent: "space-between" }}>
          <div>
            <strong>{p.nome}</strong>
            <div className="muted">{p.email}</div>
          </div>
          <div className="row">
            <button type="button" className="secondary" onClick={() => onSelect?.(p)}>
              Editar
            </button>
            <button type="button" className="danger" onClick={() => remover(p.id)}>
              Excluir
            </button>
          </div>
        </li>
      ))}
    </ul>
  );
}
