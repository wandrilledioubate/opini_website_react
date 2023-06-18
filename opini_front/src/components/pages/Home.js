import React from 'react';
import '../../App.css';
import HeroSection from '../HeroSection';
import ExplicationSection from '../ExplicationSection';
import Carrousel from '../Carrousel';
import Entreprise from '../Entreprise';

function Home() {
  return (
    <>
      <HeroSection />
      <ExplicationSection />
      <Carrousel />
      <Entreprise />
    </>
  );
}

export default Home;