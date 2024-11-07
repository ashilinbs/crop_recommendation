from flask import Flask, request, jsonify
from flask_cors import CORS 
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)  


model = joblib.load('model/crop_model.pkl')
scaler = joblib.load('model/scaler.pkl')
label_encoder = joblib.load('model/label_encoder.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    
    features = np.array([[data['N'], data['P'], data['K'], data['temperature'], data['humidity'], data['ph'], data['rainfall']]])
    
  
    features_scaled = scaler.transform(features)
    
   
    prediction = model.predict(features_scaled)
    
    
    predicted_crop = label_encoder.inverse_transform(prediction)
    
    return jsonify({'predicted_crop': predicted_crop[0]})

if __name__ == '__main__':
    app.run(debug=True)
