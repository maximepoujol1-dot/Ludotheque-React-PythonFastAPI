export const requete = async (endpoint: string, options: RequestInit = {}) => {
  const token = localStorage.getItem('access_token');
  const baseUrl = import.meta.env.VITE_API_URL;

  const headers = {
    'Content-Type': 'application/json',
    ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
    ...(options.headers || {}),
  };

  const response = await fetch(`${baseUrl}${endpoint}`, {
    ...options,
    headers,
  });

  return response.json();
};
