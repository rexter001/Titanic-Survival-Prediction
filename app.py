from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import os

app = Flask(__name__)

# Model and scaler
model = None
scaler = None

def load_or_create_model():
    """Load pre-trained model or create a demo model"""
    global model, scaler
    
    try:
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
        print("✅ Model loaded from files")
    except FileNotFoundError:
        print("⚠️ Model files not found. Using demo model...")
        # Create demo model for testing
        from sklearn.datasets import make_classification
        X_demo, y_demo = make_classification(
            n_samples=200, n_features=7, n_classes=2, random_state=42
        )
        
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_demo)
        
        model = RandomForestClassifier(n_estimators=50, random_state=42)
        model.fit(X_scaled, y_demo)
        print("✅ Demo model created")

# Load model on startup
load_or_create_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Extract features from request
        features = [
            float(data.get('pclass', 1)),
            float(data.get('sex', 0)),
            float(data.get('age', 30)),
            float(data.get('sibsp', 0)),
            float(data.get('parch', 0)),
            float(data.get('fare', 50)),
            float(data.get('embarked', 0))
        ]
        
        # Validate input
        if len(features) != 7:
            return jsonify({
                'success': False,
                'error': 'Expected 7 features'
            }), 400
        
        # Scale features
        features_scaled = scaler.transform([features])
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        probability = float(model.predict_proba(features_scaled)[0][1])
        
        # Determine survival
        if prediction == 1:
            result = "✅ Likely to Survive"
            survival_rate = probability * 100
        else:
            result = "🔴 Unlikely to Survive"
            survival_rate = (1 - probability) * 100
        
        return jsonify({
            'success': True,
            'result': result,
            'survival_probability': round(probability * 100, 2),
            'confidence': round(survival_rate, 2)
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/info', methods=['GET'])
def info():
    return jsonify({
        'name': 'Titanic Survival Prediction',
        'version': '1.0',
        'features': [
            'Passenger Class (1-3)',
            'Sex (0=Female, 1=Male)',
            'Age (years)',
            'Siblings/Spouses (SibSp)',
            'Parents/Children (Parch)',
            'Fare (ticket price)',
            'Embarked (0=C, 1=Q, 2=S)'
        ],
        'model': 'Random Forest Classifier'
    })

if __name__ == '__main__':
    app.run(debug=True)
