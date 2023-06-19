import React from 'react';
import './BarreProgression.css';

class BarreProgression extends React.Component {
    render() {
        return (
            <div className="progress-container">
                <div className="progress-bar" style={{width: `${this.props.pourcentage}%`}}></div>
                <p className="progress-text">La progression est de {this.props.pourcentage}%</p>
            </div>
        );
    }
}

export default BarreProgression;
























/* 
const BarreProgression = () => {
  const [pourcentage, setPourcentage] = useState(0);

  useEffect(() => {
    // Appel à l'API pour récupérer le pourcentage de remplissage
    // Mettez à jour le state "pourcentage" avec la valeur récupérée

    // Exemple d'appel à l'API fictive (à remplacer avec votre propre logique)
    const fetchProgressFromAPI = async () => {
      try {
        const response = await fetch('https://votre-api.com/progression');
        const data = await response.json();
        setPourcentage(data.pourcentage);
      } catch (error) {
        console.error('Erreur lors de la récupération du pourcentage de remplissage :', error);
      }
    };

    fetchProgressFromAPI();
  }, []);

  return (
    <div className="progress-bar">
      <div className="progress-bar-fill" style={{ width: `${pourcentage}%` }}></div>
    </div>
  );
};

export default BarreProgression;
*/

