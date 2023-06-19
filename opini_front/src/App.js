import React from 'react';
import Header from './components/Header';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/pages/Home';
import Footer from './components/Footer';
import TestAI from './components/pages/TestAI';
import Concept from './components/pages/Concept';

function App() {
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
}

export default App;