import React from 'react'
import { useState, useEffect } from 'react';
const services = () => {
    const [messageBackend, setMessageBackend] = useState("Chargement...");
      useEffect(() => {
        fetch("http://localhost:8000/items")
          .then(reponse => reponse.json())
          .then(donnees => {
            setMessageBackend(JSON.stringify(donnees));
          })
          .catch(erreur => console.error("Erreur de connexion:", erreur));
      }, []);

  return (
    <div>
      <div style={{ padding: "20px", textAlign: "center" }}>
        {messageBackend}
      </div>
    </div>
  )
}

export default services