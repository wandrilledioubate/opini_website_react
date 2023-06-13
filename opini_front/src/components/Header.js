import React from 'react';
// import { Link } from 'react-router-dom';
import './Header.css';
import logo from '../assets/opini_logo.png';  

const Header = () => (
  <header className="header">
    <div className="logo">
        <img src={logo} alt="Logo" className="logo" />
    </div>
    
    <nav className="navbar">
        <a href="/concept">Le concept</a>
        <a href="/testIA">Tester notre IA 🚀</a>
        <a href="/team">Notre équipe</a>
    </nav>

    <div className="cta-container">
        <a href="/concept" className="cta">Nous contacter</a>
    </div>
  </header>
);

export default Header;

