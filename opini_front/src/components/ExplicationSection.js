import React from 'react';
import { Link } from 'react-router-dom';
import './ExplicationSection.css';

function ExplicationSection() {
    return (
        <section className="explication">
            <h2 className="explication-title">Un produit profondément ancré dans son territoire</h2>
            <p className="explication-text">Dans le monde actuel de la technologie en constante évolution, un projet d'intelligence artificielle (IA) passionnant est en cours de développement pour analyser les sentiments exprimés dans les commentaires de TripAdvisor. Ce projet innovant vise à utiliser des techniques avancées de traitement du langage naturel et de machine learning pour comprendre les émotions et les sentiments cachés dans les commentaires des utilisateurs de la plateforme.</p>
            <p className="explication-text">L'objectif principal de ce projet est d'aider les entreprises du secteur du tourisme à obtenir une compréhension plus précise et approfondie des expériences de leurs clients. Les analyses générées par l'IA peuvent révéler des tendances subtiles et des motifs complexes dans les sentiments des clients qui pourraient autrement passer inaperçus.</p>
            <p className="explication-text">Les algorithmes d'apprentissage automatique utilisés dans ce projet sont formés pour identifier et catégoriser les sentiments en fonction de la tonalité du texte - par exemple, savoir si un commentaire est positif, négatif ou neutre. Ils peuvent également extraire des informations plus détaillées sur des sentiments spécifiques tels que la joie, la tristesse, la colère, le dégoût ou la surprise.</p>
            <Link to="/concept" className="explication-link">En savoir plus sur Opini</Link>
        </section>
    );
}

export default ExplicationSection;
