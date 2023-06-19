import React from 'react';
import './InputLink.css';

class InputLink extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            link: ''
        }
    }

    handleChange = (event) => {
        this.setState({
            link: event.target.value
        });
    }

    handleSubmit = () => {
        alert('Le lien ' + this.state.link + ' a été envoyé !');
    }

    render() {
        return (
            <div className="inputLink">
                <h2>Entrez le lien de votre restaurant, hôtel !</h2>
                <input 
                    type="text" 
                    placeholder="Entrer un lien ici..." 
                    value={this.state.link}
                    onChange={this.handleChange}
                />
                <button onClick={this.handleSubmit}>
                    Envoyer
                </button>
            </div>
        );
    }
}

export default InputLink;
