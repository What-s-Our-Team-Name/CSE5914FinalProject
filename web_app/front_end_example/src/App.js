import './App.css';
import configData from './config/config.json';
import axios from "axios";
import React, { useState } from 'react';

function App() {

  const [data, setData] = useState([]); // imdb data we need to query and set for
  const [loading, setLoading] = useState(false);

  const queryIMDB = async () => {
    try {
      setLoading(true);
      const result = await axios.get(configData.SERVER_URL + configData.ROUTES.IMDB); // send http request toward server
      setData(result.data.results); // update imdb data and it will automatically get rendered on web
      setLoading(false);
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <div className="App">
      <button onClick={queryIMDB}>Click to get imdb info</button>
      {/* data is empty until we click the button to query for it */}
      {loading ? <div>Loading...</div> : null}
      {data.map((val) => {
        return (<pre><div>{JSON.stringify(val)}</div></pre>);
      })}
    </div>
  );
}

export default App;