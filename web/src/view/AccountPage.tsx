import React from 'react';
import { Navigate, useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

const AccountPage = () => {
  const { isAuthenticated } = useAuth();
  const navigate = useNavigate();

  // Redirection si non connecté (comme demandé dans le contrat)
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  const handleLogout = () => {
    // Suppression du token du localStorage
    localStorage.removeItem('access_token');
    // Force la redirection vers la page de login
    navigate('/login', { replace: true });
    // Optionnel : un petit rechargement de page pour réinitialiser complètement l'état de l'app
    window.location.reload();
  };

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-4">Mon Compte</h1>
      <p className="mb-6 text-gray-600 dark:text-gray-300">
        Vous êtes connecté. Vous pouvez gérer votre session ici.
      </p>

      <button
        onClick={handleLogout}
        className="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition cursor-pointer"
      >
        Se déconnecter (Drop token)
      </button>
    </div>
  );
};

export default AccountPage;
