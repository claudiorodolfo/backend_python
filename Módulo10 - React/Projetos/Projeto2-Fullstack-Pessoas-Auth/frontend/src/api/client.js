const STORAGE_KEY = "projeto2_token";

function baseUrl() {
  const env = import.meta.env.VITE_API_URL?.replace(/\/$/, "");
  if (env) return env;
  if (import.meta.env.DEV) return "";
  return "http://127.0.0.1:8000";
}

function path(p) {
  const prefix = p.startsWith("/") ? p : `/${p}`;
  if (import.meta.env.DEV && !import.meta.env.VITE_API_URL) {
    return `/api${prefix}`;
  }
  return `${baseUrl()}${prefix}`;
}

export function getStoredToken() {
  return localStorage.getItem(STORAGE_KEY) ?? "";
}

export function setStoredToken(token) {
  if (token) localStorage.setItem(STORAGE_KEY, token);
  else localStorage.removeItem(STORAGE_KEY);
}

export async function apiFetch(urlPath, { method = "GET", body, token } = {}) {
  const headers = { "Content-Type": "application/json" };
  const t = token ?? getStoredToken();
  if (t) headers.Authorization = `Bearer ${t}`;

  const res = await fetch(path(urlPath), {
    method,
    headers,
    body: body ? JSON.stringify(body) : undefined,
  });

  if (res.status === 204) return null;

  const text = await res.text();
  const data = text ? JSON.parse(text) : null;

  if (!res.ok) {
    const detail = data?.detail;
    const msg =
      typeof detail === "string"
        ? detail
        : Array.isArray(detail)
          ? detail.map((d) => d.msg ?? JSON.stringify(d)).join("; ")
          : text || res.statusText;
    throw new Error(msg);
  }

  return data;
}

export async function apiLogin(username, password) {
  return apiFetch("/auth/login", { method: "POST", body: { username, password }, token: "" });
}

export async function apiRegister(username, password) {
  return apiFetch("/auth/register", { method: "POST", body: { username, password }, token: "" });
}
