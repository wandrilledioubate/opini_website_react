import React from 'react';
import './BarreProgression.css';

const BarreProgression = ({ data }) => {
    const random_number = data?.random_number;
    const mots_positifs = data?.mots_positifs;
    const mots_negatifs = data?.mots_negatifs;

    return (
        <div className="container">
            <h2 className="titre">D'après Opini, le taux de satisfaction de 'Nom hôtel' est :</h2>
            <div className="progressBar">
                <div className={`progressBarFill`} style={{width: `${random_number}%`}}>
                    {random_number}%
                </div>
            </div>
            <div className='word-feedback'>
              <div>
                  <h3 className="titre">Points positifs</h3>
                  <ul className="liste">
                      {mots_positifs && mots_positifs.map((mot, index) => (
                          <li key={index}>{mot}</li>
                      ))}
                  </ul>
              </div>
              <div>
                  <h3 className="titre">Points négatifs</h3>
                  <ul className="liste">
                      {mots_negatifs && mots_negatifs.map((mot, index) => (
                          <li key={index}>{mot}</li>
                      ))}
                  </ul>
              </div>
            </div>
        </div>
    );
};

export default BarreProgression;