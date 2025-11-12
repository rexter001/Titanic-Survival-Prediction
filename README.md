# Titanic Survival Prediction Web Application

A machine learning web application that predicts passenger survival on the Titanic using a Random Forest classifier.

## 🚀 Features

- **Real-time Predictions**: Get instant survival predictions for any passenger
- **Interactive UI**: User-friendly web interface
- **Multiple Input Parameters**: Age, class, sex, fare, family size, embarkation port
- **Probability Scores**: View survival probability and confidence levels
- **REST API**: Backend API for integration

## 📊 Dataset & Model

- **Dataset**: 891 passengers from the famous Titanic disaster
- **Model**: Random Forest Classifier (50 trees)
- **Features**: 7 passenger attributes
- **Accuracy**: ~82% on historical data

## 🎯 Features Used

1. **Passenger Class** - 1st, 2nd, or 3rd class
2. **Sex** - Gender (Female/Male)
3. **Age** - Age in years
4. **Siblings/Spouses (SibSp)** - Number of family members aboard
5. **Parents/Children (Parch)** - Number of family members aboard
6. **Fare** - Ticket price paid
7. **Embarked** - Port of embarkation (Cherbourg, Queenstown, Southampton)

## 🛠️ Installation

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000`

## 📡 API Endpoints

### POST /api/predict
Predict passenger survival.

**Request:**
```json
{
  "pclass": 1,
  "sex": 0,
  "age": 25,
  "sibsp": 1,
  "parch": 0,
  "fare": 100,
  "embarked": 2
}
```

**Response:**
```json
{
  "success": true,
  "result": "✅ Likely to Survive",
  "survival_probability": 75.5,
  "confidence": 75.5
}
```

### GET /api/info
Get model information and features.

## 🚢 Deploy to Vercel

1. Push to GitHub:
```bash
git add .
git commit -m "Titanic web app"
git push origin main
```

2. Connect to Vercel:
   - Go to https://vercel.com
   - Click "Add New Project"
   - Select your GitHub repository
   - Click "Deploy"

Your app will be live at `https://your-project-name.vercel.app`

## 📁 Project Structure

```
Titanic_Survival_Prediction/
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── vercel.json              # Vercel configuration
├── runtime.txt              # Python version
├── Titanic_Survival_Prediction.ipynb  # Original notebook
├── templates/
│   └── index.html           # Frontend
└── static/
    ├── style.css            # Styling
    └── script.js            # Frontend logic
```

## 🔧 Technologies

- **Backend**: Flask, Python, scikit-learn
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Vercel

## 📝 Author

Khaja Masthan Shaik (rexter001)
