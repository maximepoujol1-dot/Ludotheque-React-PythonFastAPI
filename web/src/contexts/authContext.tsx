import React, { createContext, useContext, useState, ReactNode } from 'react';

export interface User {
  id?: number;
  email: string;
  disabled?: boolean;
}

interface AuthContextType {
  token: string | null;
  user: User | null;
  login: (accessToken: string) => void;
  setCurrentUser: (userData: User) => void;
  logout: () => void;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [token, setToken] = useState<string | null>(() => localStorage.getItem('access_token'));
  const [user, setUser] = useState<User | null>(() => {
    const saved = localStorage.getItem('current_user');
    return saved ? JSON.parse(saved) : null;
  });

  const login = (accessToken: string) => {
    setToken(accessToken);
    localStorage.setItem('access_token', accessToken);
  };

  const setCurrentUser = (userData: User) => {
    setUser(userData);
    localStorage.setItem('current_user', JSON.stringify(userData));
  };

  const logout = () => {
    setToken(null);
    setUser(null);
    localStorage.removeItem('access_token');
    localStorage.removeItem('current_user');
  };

  return (
    <AuthContext.Provider value={{ token, user, login, setCurrentUser, logout, isAuthenticated: !!token }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error("useAuth doit être dans AuthProvider");
  return context;
};
