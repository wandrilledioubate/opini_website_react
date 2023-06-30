import React from 'react';
import './BarreProgression.css';

const BarreProgression = ({ data }) => {
    const taux_satisfaction = data?.taux_satisfaction;
    const points_positifs = data?.points_positifs;
    const points_negatifs = data?.points_negatifs;

    return (
        <div className="container">
            <h2 className="titre">D'après Opini, le taux de satisfaction est :</h2>
            <div className="progressBar">
                <div className={`progressBarFill`} style={{width: `${taux_satisfaction}%`}}>
                    {taux_satisfaction}%
                </div>
            </div>
            <div className='word-feedback'>
              <div>
                  <h3 className="titre">Points positifs</h3>
                  <ul className="liste">
                      {points_positifs && points_positifs.map((mot, index) => (
                          <li key={index}>{mot}</li>
                      ))}
                  </ul>
              </div>
              <div>
                  <h3 className="titre">Points négatifs</h3>
                  <ul className="liste">
                      {points_negatifs && points_negatifs.map((mot, index) => (
                          <li key={index}>{mot}</li>
                      ))}
                  </ul>
              </div>
            </div>
        </div>
    );
};

export default BarreProgression;