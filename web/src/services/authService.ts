import { requete } from './httpClient';

export const loginUser = async (email: string, password: string) => {
  const formData = new URLSearchParams();
  formData.append('username', email);
  formData.append('password', password);

  const data = await requete('/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formData.toString()
  });

  // Gestion des erreurs renvoyées par FastAPI (401, 422, etc.)
  if (data.detail || data.message || data.erreur) {
    throw new Error(data.detail || data.message || data.erreur?.message || "Erreur d'authentification");
  }

  return data;
};
