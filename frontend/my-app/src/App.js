import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const App = () => {
    const [N, setN] = useState('');
    const [P, setP] = useState('');
    const [K, setK] = useState('');
    const [temperature, setTemperature] = useState('');
    const [humidity, setHumidity] = useState('');
    const [ph, setPh] = useState('');
    const [rainfall, setRainfall] = useState('');
    const [predictedCrop, setPredictedCrop] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        try {
            const response = await axios.post('http://127.0.0.1:5000/predict', {
                N: parseFloat(N),
                P: parseFloat(P),
                K: parseFloat(K),
                temperature: parseFloat(temperature),
                humidity: parseFloat(humidity),
                ph: parseFloat(ph),
                rainfall: parseFloat(rainfall),
            });
            setPredictedCrop(`🌾 Recommended Crop: ${response.data.predicted_crop}`);
        } catch (error) {
            console.error('Error predicting crop:', error);
            setError('❌ Failed to predict crop. Please try again.');
        }
    };

    return (
        <div className="app-container">
            <h1>🌱 Crop Recommendation System 🌱</h1>
            <form onSubmit={handleSubmit}>
                <input type="number" placeholder="Nitrogen (N)" value={N} onChange={(e) => setN(e.target.value)} required />
                <input type="number" placeholder="Phosphorus (P)" value={P} onChange={(e) => setP(e.target.value)} required />
                <input type="number" placeholder="Potassium (K)" value={K} onChange={(e) => setK(e.target.value)} required />
                <input type="number" placeholder="Temperature (°C)" value={temperature} onChange={(e) => setTemperature(e.target.value)} required />
                <input type="number" placeholder="Humidity (%)" value={humidity} onChange={(e) => setHumidity(e.target.value)} required />
                <input type="number" placeholder="pH Level" value={ph} onChange={(e) => setPh(e.target.value)} required />
                <input type="number" placeholder="Rainfall (mm)" value={rainfall} onChange={(e) => setRainfall(e.target.value)} required />
                <button type="submit">Get Recommendation</button>
            </form>
            {predictedCrop && <p className="result">{predictedCrop}</p>}
            {error && <p className="error">{error}</p>}
        </div>
    );
};

export default App;
