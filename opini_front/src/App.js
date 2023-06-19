import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/pages/Home';
import Footer from './components/Footer';
import TestAI from './components/pages/TestAI';
import Concept from './components/pages/Concept';
import logo from './assets/opini_logo.png';


const App = () => {
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const timer = setTimeout(() => {
            setLoading(false);
        }, 2000);

        return () => clearTimeout(timer);
    }, []);

    if (loading) {
        return <img src={logo} className="logo_anim" alt="logo" />;
    }

    return (
      <>
        <Router>
          <Header />
          <Routes>
            <Route path='/' element={<Home />} />
            <Route path='/testIA' element={<TestAI />} />
            <Route path='/concept' element={<Concept />} />
          </Routes>
          <Footer />
        </Router>
      </>
    );
};

export default App;