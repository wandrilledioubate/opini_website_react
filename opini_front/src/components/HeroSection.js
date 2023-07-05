import React from 'react';
import './HeroSection.css';
import play_icon from '../assets/play_icon.svg';  
import { Link } from 'react-router-dom';


function HeroSection() {
    return (
        <section className="hero">
            <h1 className="hero-title">La solution pour connaître <span class="gradient-text">vraiment</span> l’avis des utilisateurs !</h1>
            <p className="hero-text">  </p>
            <div className="hero-cta">
                <a href="https://www.youtube.com/watch?v=VFR6LtEKBVY&ab_channel=Mizuno11" target="_blank" rel="noopener noreferrer">
                    <button className="cta-button-1">
                        <img src={play_icon} alt="Play Icon" className="button-icon" />
                        <span>Regarder la démo</span>
                    </button>
                </a>
                <Link to="/testIA">
                    <button className="cta-button-2">Tester notre notre IA 🚀</button>
                </Link>            
            </div>
        </section>
    );
}

export default HeroSection;
