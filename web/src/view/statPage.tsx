import React from 'react'
import { Navigate } from 'react-router-dom';

const statPage = () => {
   const token = localStorage.getItem('access_token');

  if (!token) {
    return <Navigate to="/login" replace />;
  }

  return (
    <div>statPage</div>
  )
}

export default statPage