import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { apiRegister } from "../api/client.js";

export default function RegisterPage() {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [submitting, setSubmitting] = useState(false);

  async function onSubmit(e) {
    e.preventDefault();
    setError("");
    setSubmitting(true);
    try {
      await apiRegister(username.trim(), password);
      navigate("/login", { replace: true });
    } catch (err) {
      setError(err.message ?? String(err));
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <main>
      <h1>Criar conta</h1>

      <form onSubmit={onSubmit} className="card">
        <label>
          Usuário
          <input value={username} onChange={(e) => setUsername(e.target.value)} required autoComplete="username" />
        </label>
        <label>
          Senha
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            autoComplete="new-password"
          />
        </label>
        {error ? <p className="error">{error}</p> : null}
        <div className="row">
          <button type="submit" disabled={submitting}>
            {submitting ? "Registrando…" : "Registrar"}
          </button>
          <Link to="/login">Já tenho conta</Link>
        </div>
      </form>
    </main>
  );
}
