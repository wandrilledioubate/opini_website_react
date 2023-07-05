import React, { useState } from 'react';
import axios from 'axios';
import BarreProgression from './BarreProgression';
import './InputLink.css';

const InputLink = () => {
  const [url, setUrl] = useState('');
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false); // Ajout du state pour le chargement

  const handleSubmit = (event) => {
    event.preventDefault();
    setIsLoading(true); // Définir le chargement sur true lors de la soumission du formulaire
    axios
      .post('http://127.0.0.1:5000/predict', { url })
      .then((response) => {
        setData(response.data);
        setError(null);
      })
      .catch((error) => {
        console.error(`Erreur: ${error}`);
        setError("Une erreur s'est produite lors de la récupération des données");
        setData(null);
      })
      .finally(() => {
        setIsLoading(false); // Définir le chargement sur false une fois que la requête est terminée
      });
  };

  return (
    <div>
      <div className="input-component">
        <h2 className="input-title-1">Tester notre IA !</h2>
        <h3 className="input-title-2">
          Rentrez le lien de votre annonce Tripadvisor pour connaître sa satisfaction !
        </h3>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            className="input-search"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
          />
          <button type="submit">Envoyer</button>
        </form>
        {error && <div className="error">{error}</div>}
        {isLoading && <div className="loader"></div>} {/* Afficher la roue de chargement si isLoading est vrai */}
      </div>
      {data && <BarreProgression data={data} />}
    </div>
  );
};

export default InputLink;
