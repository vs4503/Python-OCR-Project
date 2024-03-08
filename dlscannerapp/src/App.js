import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  //set a Javascript object to store and use data
  const [data, setData] = useState({
    name: "",
    age: "",
    date: "",
    hometown: "",
  });

  //Use fetch to fetch the data from the flask server redirected by proxy
  useEffect(() => {
    fetch('/data').then(response => response.json()
    .then((data) => {
      setData({
        name: data.Name,
        age: data.Age,
        date: data.Date,
        hometown: data.HomeTown,
      });
    })
    );
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1> React and Flask</h1>
        <p> {data.name} </p>
        <p> {data.age} </p>
        <p> {data.date} </p>
        <p> {data.hometown} </p>
      </header>
    </div>
  );
}

export default App;
