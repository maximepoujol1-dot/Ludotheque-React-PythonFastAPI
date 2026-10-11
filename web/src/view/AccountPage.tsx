import { Navigate, useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import Avatar from '../components/Avatar';
import Card from '../components/Card';

function usernameByEmail(email: string | null | undefined, separator: string): string {
    if (!email) {
        return 'no found';
    }

    const index = email.indexOf(separator);
    if (index <= 0) {
        return email;
    }

    return email.slice(0, index);
}

const AccountPage = () => {
  const { user, isAuthenticated, logout } = useAuth();
  const navigate = useNavigate();

  // Redirection si non connecté (comme demandé dans le contrat)
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  const handleLogout = () => {
    logout();
    navigate('/login', { replace: true });
  };

  return (
    <div className="p-8">
      <Card title={'User : '} style={'flex w-full max-w-none flex-col gap-4 p-5 sm:p-6 card bg-white dark:bg-dark-surface shadow-xl border border-gray-200 dark:border-white/10 border-t-4 border-t-green-500 rounded-2xl'} >
        <div className="grid w-full grid-cols-1 items-stretch gap-4 md:grid-cols-[minmax(180px,1fr)_2fr]">
          <Card title={''} style={'flex min-h-48 w-full items-center justify-center p-5 card bg-white dark:bg-dark-surface shadow-md border border-gray-200 dark:border-white/10 rounded-2xl'} >
            <Avatar/>
          </Card>
          <Card title={''} style={'flex min-h-48 w-full flex-col gap-3 p-5 card bg-white dark:bg-dark-surface shadow-md border border-gray-200 dark:border-white/10 rounded-2xl'} >
            <h1 className="text-lg font-semibold text-gray-900 dark:text-white">Information : </h1>
            <p> - id : {user?.id ?? 'no found'}</p>
            <p> - email : {user?.email ?? 'no found'}</p>
            <p> - Userame : { usernameByEmail(user?.email, "@")}</p>
            <p> </p>
          </Card>
        </div>
      </Card>
      <br/>
      <Card title={'Action :'} style={'flex flex-row flex-wrap items-center gap-3 w-full max-w-none p-5 sm:p-6 card bg-white dark:bg-dark-surface shadow-xl border border-gray-200 dark:border-white/10 border-t-4 border-t-green-500 rounded-2xl'} >
        <button onClick={() => navigate('/')} className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition cursor-pointer"> see catalogue </button>
        <button onClick={() => navigate('/collection')} className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition cursor-pointer"> see my collection </button>
        <button onClick={handleLogout} className="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition cursor-pointer"> Logout </button>
      </Card>      
    </div>
  );
};

export default AccountPage;
