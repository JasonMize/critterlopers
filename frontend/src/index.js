import 'bootstrap/dist/css/bootstrap.css';
import './styles/App.css';

import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Comic from './components/Comic';
import About from './components/About';
import Archive from './components/Archive';



ReactDOM.render(
  <Router>
    <div>
      <Route path="/comic" component={Comic} />
      <Route path="/about" component={About} />
      <Route path="/archive" component={Archive} />
    </div>
  </Router>,
  document.getElementById('root')
);

