import { useState } from "react";
import { Navigate, Route, Routes } from "react-router-dom";
import PessoaForm from "./components/PessoaForm.jsx";
import PessoaList from "./components/PessoaList.jsx";
import { useAuth } from "./context/AuthContext.jsx";
import LoginPage from "./pages/LoginPage.jsx";
import RegisterPage from "./pages/RegisterPage.jsx";

function RequireAuth({ children }) {
  const { isAuthenticated } = useAuth();
  if (!isAuthenticated) return <Navigate to="/login" replace />;
  return children;
}

function PessoasScreen() {
  const { logout } = useAuth();
  const [refreshKey, setRefreshKey] = useState(0);
  const [editing, setEditing] = useState(null);

  function bump() {
    setRefreshKey((k) => k + 1);
  }

  return (
    <main>
      <div className="topbar">
        <h1 style={{ margin: 0 }}>Pessoas</h1>
        <button type="button" className="secondary" onClick={logout}>
          Sair
        </button>
      </div>

      <p className="muted">
        Backend FastAPI em <code>127.0.0.1:8000</code>. Em dev, o Vite usa proxy <code>/api</code>.
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

export default function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route path="/register" element={<RegisterPage />} />
      <Route
        path="/"
        element={
          <RequireAuth>
            <PessoasScreen />
          </RequireAuth>
        }
      />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}
