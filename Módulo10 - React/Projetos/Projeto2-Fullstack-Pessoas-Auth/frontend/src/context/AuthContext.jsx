import { createContext, useContext, useMemo, useState } from "react";
import { apiLogin, getStoredToken, setStoredToken } from "../api/client.js";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [token, setToken] = useState(() => getStoredToken());

  const login = async (username, password) => {
    const data = await apiLogin(username, password);
    setStoredToken(data.access_token);
    setToken(data.access_token);
  };

  const logout = () => {
    setStoredToken("");
    setToken("");
  };

  const value = useMemo(() => ({ token, login, logout, isAuthenticated: Boolean(token) }), [token]);

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth deve ser usado dentro de AuthProvider");
  return ctx;
}
