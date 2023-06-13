import React from 'react';
import { Link } from 'react-router-dom';
import './ExplicationSection.css';

function ExplicationSection() {
    return (
        <section className="explication">
            <h2 className="explication-title">Titre de la section d'explication</h2>
            <p className="explication-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse varius enim in eros elementum tristique. Duis cursus, mi quis viverra ornare, eros dolor interdum nulla, ut commodo diam libero vitae erat.</p>
            <p className="explication-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse varius enim in eros elementum tristique. Duis cursus, mi quis viverra ornare, eros dolor interdum nulla, ut commodo diam libero vitae erat.</p>
            <Link to="/concept" className="explication-link">En savoir plus sur le concept</Link>
        </section>
    );
}

export default ExplicationSection;
