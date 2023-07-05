import React from 'react';
import Team from './Team';
import WandrillePhoto from '../assets/wandrillepic.jpg';
import CarlaPhoto from '../assets/carlapic.jpg';
import MatthieuPhoto from '../assets/matthieupic.jpg';
import SalahPhoto from '../assets/salahpic.jpg';
import NassimPhoto from '../assets/nassimpic.jpg';
import ElisaPhoto from '../assets/elisapic.jpg';
import '../App.css';

const TeamPage = () => {
    const teamMembers = [
        {
          name: 'Wandrille',
          photo: WandrillePhoto,
          description: 'Développement du site internet et de API',
        },
        {
          name: 'Carla',
          photo: CarlaPhoto,
          description: 'Développement du modèle de Deep Learning',
        },
        {
            name: 'Matthieu',
            photo: MatthieuPhoto,
            description: 'Développement du modèle de Deep Learning',
        },
        {
            name: 'Salah',
            photo: SalahPhoto,
            description: 'Développement du script de scrapping',
        },
        {
            name: 'Nassim',
            photo: NassimPhoto,
            description: 'Développement du script de scrapping',
        },
        {
            name: 'Elisa',
            photo: ElisaPhoto,
            description: 'Rédaction des livrables et des UML',
        },

      ];
    
      return (
        <div className="app-container">
          <Team members={teamMembers} />
        </div>
      );
    };

export default TeamPage;
