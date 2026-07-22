import { useState } from "react";
import PessoaForm from "./components/PessoaForm.jsx";
import PessoaList from "./components/PessoaList.jsx";

export default function App() {
  const [refreshKey, setRefreshKey] = useState(0);
  const [editing, setEditing] = useState(null);

  function bump() {
    setRefreshKey((k) => k + 1);
  }

  return (
    <main>
      <h1>Projeto1 — Pessoas (React → FastAPI)</h1>
      <p className="muted">
        Backend: Módulo9 <code>Projetos/Projeto1</code> em <code>127.0.0.1:8000</code>. Em dev, este app usa
        proxy <code>/api</code>.
      </p>

      <PessoaForm
        editing={editing}
        onSaved={() => {
          setEditing(null);
          bump();
        }}
      />

      {editing ? (
        <p className="muted">
          Editando <strong>{editing.nome}</strong> —{" "}
          <button type="button" className="secondary" onClick={() => setEditing(null)}>
            Cancelar edição
          </button>
        </p>
      ) : null}

      <h2 style={{ fontSize: "1.05rem" }}>Lista</h2>
      <PessoaList refreshKey={refreshKey} onSelect={setEditing} onChanged={bump} />
    </main>
  );
}
