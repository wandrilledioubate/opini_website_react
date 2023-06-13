// Entreprise.js

import React from 'react';
import './Entreprise.css';
import tripadvisor from '../assets/tripadvisor.png';
import amazon from '../assets/amazon.png';
import booking from '../assets/booking.png';
import airbnb from '../assets/airbnb.png';

function Entreprise() {
  return (
    <div className="entreprise">
      <h1 className="titre">Titre de la page Entreprise</h1>
      <div className="logo-container">
        <div className="logo-card">
          <img src={tripadvisor} alt="logo1" className="logo"/>
        </div>
        <div className="logo-card">
          <img src={amazon} alt="logo2" className="logo"/>
        </div>
        <div className="logo-card">
          <img src={booking} alt="logo3" className="logo"/>
        </div>
        <div className="logo-card">
          <img src={airbnb} alt="logo4" className="logo"/>
        </div>
      </div>
    </div>
  );
}

export default Entreprise;
