import React from 'react';
import Header from './components/Header';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/pages/Home';
import TestAI from './components/pages/TestAI';

function App() {
  return (
    <>
      <Router>
        <Header />
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/testAI' element={<TestAI />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;