import React, { useState } from 'react';
import axios from 'axios';
import BarreProgression from './BarreProgression';
import './InputLink.css';

const InputLink = () => {
    const [url, setUrl] = useState('');
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);

    const handleSubmit = (event) => {
        event.preventDefault();
        axios.post('http://127.0.0.1:5000/randomize', { url })
            .then(response => {
                setData(response.data);
                setError(null);
            })
            .catch(error => {
                console.error(`Erreur: ${error}`);
                setError('Une erreur s\'est produite lors de la récupération des données');
                setData(null);
            });
    };

    return (
        <div>
            <div className='input-component'>
                <h2 className="input-title-1">Tester notre IA !</h2>
                <h3 className="input-title-2">Rentrez le lien de votre annonce Tripadvisor pour connaître sa satisfaction !</h3>
                <form onSubmit={handleSubmit}>
                    <input type="text" value={url} onChange={(e) => setUrl(e.target.value)} />
                    <button type="submit">Envoyer</button>
                </form>
                {error && <div className="error">{error}</div>}
                </div>
                {data && <BarreProgression data={data} />}
        </div>
    );
};

export default InputLink;
