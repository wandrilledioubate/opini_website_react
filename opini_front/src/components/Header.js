import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';
import logo from '../assets/opini_logo.png';  

const Header = () => (
  <header className="header">
    <div className="logo">
        <Link to="/">
          <img src={logo} alt="Logo" className="logo" />
        </Link>
    </div>
    
    <nav className="navbar">
        <Link to="/concept">Le concept</Link>
        <Link to="/testIA">Testez notre IA 🚀</Link>
        <Link to="/team">Notre équipe</Link>
    </nav>

    <div className="cta-container">
      <a href="mailto:wandrille.dioubate@efrei.net,salah.boughanmi@efrei.net" className="cta">
          Nous contacter
      </a>
    </div>
  </header>
);

export default Header;


