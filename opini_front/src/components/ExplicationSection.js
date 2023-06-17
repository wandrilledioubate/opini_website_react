import React from 'react';
import { Link } from 'react-router-dom';
import './ExplicationSection.css';

function ExplicationSection() {
    return (
        <section className="explication">
            <h2 className="explication-title">Un produit profondément ancré dans son territoire</h2>
            <p className="explication-text">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting.</p>
            <p className="explication-text">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting.</p>
            <Link to="/concept" className="explication-link">En savoir plus sur le concept</Link>
        </section>
    );
}

export default ExplicationSection;
