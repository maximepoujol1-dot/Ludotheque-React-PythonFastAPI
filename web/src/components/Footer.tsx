import React from 'react'
import { Link } from 'react-router-dom'


const Footer = () => {
  return (
    <footer className="fixed bottom-0 left-0 w-full bg-gray-800 text-gray-300 ">
      <div className="container mx-auto flex justify-between ">
        
        <div>
          <br/>
          <h1>Navigation :</h1>
          <br/>
          <ul className='space-y-2'>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/collection">Collection</Link></li>
            <li><Link to="/account">Account</Link></li>
          </ul>
        </div>

        <div>
          <br/>
          <h1>Legals :</h1>
          <br/>
          <ul className='space-y-2'>
            <li>Conditions d'utilisation</li>
            <li>confidentialité</li>
            <li>Mentions légales</li>
          </ul>
        </div>

        <div>
          <br/>
          <h1>other links :</h1>
          <br/>
          <ul className='space-y-2'>
            <li><a href="https://github.com/maximepoujol1-dot/Ludotheque-React-PythonFastAPI" className="hover:text-white transition-colors">Repository</a></li>
            <li><a href="https://github.com/maximepoujol1-dot" className="hover:text-white transition-colors">Github maxime</a></li>
            <li><a href="https://github.com/poketoto45" className="hover:text-white transition-colors">Github Thomas</a></li>
          </ul>
        </div>
      </div>
      <br/>
    </footer>
  )
}

export default Footer