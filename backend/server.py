# Required Libraries
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Step 1: Create the 'model' directory if it doesn't exist
os.makedirs('model', exist_ok=True)

# Step 2: Load Dataset
data = pd.read_csv('Crop_recommendation.csv')  # Ensure the path is correct

# Step 3: Preprocessing
label_encoder = LabelEncoder()
data['label'] = label_encoder.fit_transform(data['label'])  # Encode crop labels

# Separate features (X) and target (y)
X = data.drop(['label'], axis=1)  # Features
y = data['label']  # Target (Encoded Crop Labels)

# Scale the feature values for better model performance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Step 4: Train the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Evaluate the Model's Performance
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred) * 100  # Accuracy in percentage
print(f'Model Accuracy: {accuracy:.2f}%')

# Step 6: Save the Model, Scaler, and Label Encoder using Joblib
joblib.dump(model, 'model/crop_model.pkl')
joblib.dump(scaler, 'model/scaler.pkl')
joblib.dump(label_encoder, 'model/label_encoder.pkl')

print("Model, scaler, and label encoder saved successfully!")
