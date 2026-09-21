import {Routes, Route } from "react-router-dom"
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

  return (
    <>
      <Navbar/>
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
