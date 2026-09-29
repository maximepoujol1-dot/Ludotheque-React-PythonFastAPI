import React from 'react'
import { Link } from 'react-router-dom'

const titleStyle = 'text-white font-semibold uppercase tracking-wider text-sm mb-4'
const linkStyle = 'hover:text-orange-400 transition-colors'

const Footer = () => {
  return (
    <footer className="bg-gray-900 text-gray-400 w-full mt-auto border-t border-gray-800">
      <div className="container mx-auto px-6 py-10 grid grid-cols-1 sm:grid-cols-3 gap-8 text-sm">
        
        <div>
          <br/>
          <h1 className={titleStyle}>Navigation :</h1>
          <br/>
          <ul className='space-y-2'>
            <li><Link to="/" className={linkStyle}>Home</Link></li>
            <li><Link to="/collection" className={linkStyle}>Collection</Link></li>
            <li><Link to="/account" className={linkStyle} >Account</Link></li>
          </ul>
        </div>

        <div>
          <br/>
          <h1 className={titleStyle}>Legals :</h1>
          <br/>
          <ul className='space-y-2'>
            <li><Link to="/legal" className={linkStyle}>Conditions d'utilisation</Link></li>
            <li><Link to="/legal" className={linkStyle}>confidentialité</Link></li>
            <li><Link to="/legal" className={linkStyle}>Mentions légales</Link></li>
          </ul>
        </div>

        <div>
          <br/>
          <h1 className={titleStyle}>other links :</h1>
          <br/>
          <ul className='space-y-2'>
            <li><a href="https://github.com/maximepoujol1-dot/Ludotheque-React-PythonFastAPI" className={linkStyle}>Repository</a></li>
            <li><a href="https://github.com/Huldraine/Micromaniac" className={linkStyle}>premier Micromaniac</a></li>
            <li><a href="https://github.com/maximepoujol1-dot" className={linkStyle}>Github maxime</a></li>
            <li><a href="https://github.com/poketoto45" className={linkStyle}>Github Thomas</a></li>
          </ul>
        </div>
      </div>
      <br/>
    </footer>
  )
}

export default Footer 