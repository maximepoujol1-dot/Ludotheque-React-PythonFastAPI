import { useState, useEffect } from 'react';
import { Routes, Route } from "react-router-dom"
import './App.css'
import NotFoundPage from "./view/NotFoundPage"
import LoginPage from "./view/LoginPage"
import AccountPage from "./view/AccountPage"
import HomePage from "./view/HomePage"
import CollectionPage from "./view/CollectionPage"
import Navbar from "./components/Navbar"
import Footer from "./components/Footer"
import RegisterPage from "./view/RegisterPage"

function App() {
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
    <>
      <Navbar/>
      <div style={{ padding: "20px", textAlign: "center" }}>
        {messageBackend}
      </div>
      <Routes>
        <Route path="/" element={<HomePage/>}/>
        <Route path="/collection" element={<CollectionPage/>}/>
        <Route path="/account" element={<AccountPage/>}/>
        <Route path="/login" element={<LoginPage/>}/>
        <Route path="/register" element={<RegisterPage/>}/>
        <Route path="*" element={<NotFoundPage/>}/>
      </Routes>
      <Footer/>
    </>
  )
}

export default App
