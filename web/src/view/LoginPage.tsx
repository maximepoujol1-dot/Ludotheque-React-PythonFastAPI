import { useState } from 'react';
import { Link, Navigate } from 'react-router-dom';
import Card from '../components/Card';
import { useAuth } from '../contexts/AuthContext';

const tabBase = "px-6 py-2 font-semibold transition-colors cursor-pointer border-b-2"
const cardStyle = "flex flex-col w-full max-w-sm p-8 card bg-white dark:bg-dark-surface shadow-xl border border-gray-200 dark:border-white/10 border-t-4 border-t-green-500 rounded-2xl"
const titleStyle = "text-sm font-semibold text-gray-600 dark:text-gray-300 mt-2"
const inputStyle = "input validator w-full bg-gray-50 dark:bg-white/5 text-gray-900 dark:text-white placeholder:text-gray-400 dark:placeholder:text-gray-500 border border-gray-300 dark:border-white/10 rounded-lg px-4 py-2 transition focus:outline-none focus:bg-white dark:focus:bg-white/10 focus:border-green-500 focus:ring-2 focus:ring-green-200 dark:focus:ring-green-500/30"
const buttonStyle = "mt-6 w-full py-2 rounded-lg bg-green-500 text-white font-semibold shadow-md transition hover:bg-green-600 active:scale-95 cursor-pointer"

const LoginPage = () => {
  const { login, isAuthenticated } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  if (isAuthenticated) {
    return <Navigate to="/account" replace />;
  }

  const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault();
      setError('');

      try {
        // FastAPI / OAuth2PasswordRequestForm attend du x-www-form-urlencoded avec "username" et "password"
        const formData = new URLSearchParams();
        formData.append('username', email);
        formData.append('password', password);

        const response = await fetch("http://localhost:8000/auth/login", {
          method: 'POST',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          body: formData.toString()
        });

        const data = await response.json();
        console.log("Données JSON reçues du serveur :", data);

        if (!response.ok) {
          throw new Error(data?.detail || data?.message || "Erreur d'authentification");
        }

        const token = data.access_token || data.token || data.accessToken;

        if (token) {
          login(token);
        } else {
          setError('Token manquant dans la réponse du serveur');
        }
      } catch (err: any) {
        console.error("Erreur attrapée :", err);
        setError(err.message || 'Identifiants incorrects');
      }
    };

  return (
    <div className="flex min-h-screen flex-col md:flex-row items-center justify-center">
      <div className="flex flex-1 flex-col items-center justify-center px-4 py-12">
        <div className="flex flex-col md:flex-row justify-center items-stretch gap-6 w-full max-w-3xl min-h-[500px]">

          <Card title={"Login"} style={cardStyle}>
            <form onSubmit={handleSubmit} className="flex flex-col gap-2 mt-4">

              {error && <p className="text-red-500 text-sm font-semibold text-center">{error}</p>}

              <h2 className={titleStyle}>Email</h2>
              <input
                className={inputStyle}
                type="email"
                required
                placeholder="mail@site.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />

              <h2 className={titleStyle}>Password</h2>
              <input
                className={inputStyle}
                type="password"
                required
                placeholder="your password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />

              <button type="submit" className={buttonStyle}>Submit</button>

              <div className="flex justify-center items-center gap-2 mt-8">
                <Link to="/register"><li className={tabBase}>Register</li></Link>
              </div>
            </form>
          </Card>
        </div>
      </div>
      <div className="flex flex-1 items-center justify-center p-8">
        <img src="src/assets/font.png" alt="Illustration de connexion" className="h-full w-full object-cover rounded-2xl"/>
      </div>
    </div>
  )
}

export default LoginPage;
