import { Navigate } from 'react-router-dom';

export default function AccountPage() {
  const token = localStorage.getItem('access_token');

  if (!token) {
    return <Navigate to="/login" replace />;
  }

  return (
    <div>
      <h1>Mon Compte</h1>
      {/* futur contenu utilisateur */}
      <p>Bienvenue ! Si tu vois ça, c'est que tu as un token.</p>
    </div>
  );
}
