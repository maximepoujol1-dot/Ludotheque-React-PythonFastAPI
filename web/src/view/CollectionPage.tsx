import React from 'react'
import { Navigate } from 'react-router-dom';
const CollectionPage = () => {
  const token = localStorage.getItem('access_token');

  if (!token) {
    return <Navigate to="/login" replace />;
  }

  return (
    <div>CollectionPage</div>
  )
}

export default CollectionPage