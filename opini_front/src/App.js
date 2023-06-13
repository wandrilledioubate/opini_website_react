import React from 'react';
import Header from './components/Header';
import './App.css';
import { BrowserRouter as Router } from 'react-router-dom';
import HeroSection from './components/HeroSection';
import ExplicationSection from './components/ExplicationSection';
import Carrousel from './components/Carrousel';
import Entreprise from './components/Entreprise';

function App() {
  return (
    <>
      <Router>
        <Header />
        <HeroSection />
        <ExplicationSection />
        <Carrousel />
        <Entreprise /> 
      </Router>
    </>
  );
}

export default App;