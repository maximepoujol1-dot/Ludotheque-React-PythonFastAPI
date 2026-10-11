import { requete } from './httpClient';
import type { User } from '../contexts/AuthContext';

export const getCurrentUser = async (token: string): Promise<User> => {
  const data = await requete('/auth/me', {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (typeof data?.id !== 'number' || typeof data?.email !== 'string') {
    throw new Error(data?.detail || "Impossible de récupérer le profil utilisateur");
  }

  return {
    id: data.id,
    email: data.email,
    ...(typeof data.disabled === 'boolean' ? { disabled: data.disabled } : {}),
  };
};

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
