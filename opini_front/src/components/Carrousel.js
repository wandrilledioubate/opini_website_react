import React from 'react';
import { Carousel } from 'react-responsive-carousel';
import 'react-responsive-carousel/lib/styles/carousel.min.css';
import './Carrousel.css';
import logo1 from '../assets/carrousel1.png';  
import logo2 from '../assets/carrousel2.png';  
import logo3 from '../assets/carrousel3.png';  


function Carrousel() {
    return (
        <section className="carrousel-section">
            <h2 className="carrousel-title">Titre du carrousel</h2>
            <Carousel
                showArrows={false}
                showThumbs={false}
                showStatus={false}
                infiniteLoop
                autoPlay
                interval={3000}
            >
                <div>
                    <img src={logo1} alt="Slide 1" />
                </div>
                <div>
                    <img src={logo2} alt="Slide 2" />
                </div>
                <div>
                    <img src={logo3} alt="Slide 3" />
                </div>
                <div>
                    <img src={logo3} alt="Slide 4" />
                </div>
            </Carousel>
        </section>
    );
}

export default Carrousel;
