# Titanic Survival Prediction

A machine learning project to predict passenger survival on the Titanic using classification models.

## Overview

This project implements predictive models to determine which passengers survived the Titanic disaster based on their characteristics (age, sex, passenger class, etc.). It compares the performance of multiple machine learning algorithms on the famous Titanic dataset.

## Dataset

The project uses the **Titanic Dataset**, which contains information about 891 passengers including:
- **PassengerId**: Unique identifier
- **Pclass**: Passenger class (1st, 2nd, 3rd)
- **Sex**: Gender (male/female)
- **Age**: Age in years
- **SibSp**: Number of siblings/spouses aboard
- **Parch**: Number of parents/children aboard
- **Fare**: Ticket fare
- **Embarked**: Port of embarkation
- **Cabin**: Cabin number (many missing)
- **Survived**: Target variable (0 = No, 1 = Yes)

## Data Processing

1. **Missing Value Handling**:
   - Age: Filled with median value
   - Embarked: Filled with mode value
   - Cabin: Dropped due to excessive missing values

2. **Feature Encoding**:
   - Sex: Converted to binary (male=1, female=0)
   - Embarked: Label encoded

3. **Feature Selection**:
   - Used features: Pclass, Sex, Age, SibSp, Parch, Fare, Embarked

## Models

The project implements and compares two classification models:

### 1. **Logistic Regression**
- A linear classification model
- Fast and interpretable
- Good baseline for comparison

### 2. **Random Forest**
- An ensemble learning method
- Captures non-linear relationships
- More robust to overfitting

## Results

Models are evaluated using:
- **Accuracy Score**: Overall correctness of predictions
- **Confusion Matrix**: True positives, true negatives, false positives, false negatives

The Random Forest model typically outperforms Logistic Regression on this dataset.

## Workflow

1. **Data Loading**: Import Titanic dataset from CSV
2. **Exploratory Data Analysis**: Understand data distribution and missing values
3. **Data Preprocessing**: Handle missing values and encode categorical features
4. **Train-Test Split**: Split data (80% train, 20% test)
5. **Model Training**: Fit both Logistic Regression and Random Forest models
6. **Evaluation**: Compare model performance using accuracy and confusion matrices
7. **Visualization**: Display results through confusion matrix plots

## Requirements

- Python 3.x
- pandas
- scikit-learn
- matplotlib

## Usage

1. Upload the Titanic dataset (`Titanic-Dataset.csv`)
2. Run the notebook cells sequentially
3. View model performance metrics and visualizations

## Project Structure

```
Titanic_Survival_Prediction/
├── Titanic_Survival_Prediction.ipynb  # Main project notebook
└── README.md                          # Project documentation
```

## Future Enhancements

- Feature engineering (creating new features like family size, title extraction)
- Hyperparameter tuning
- Additional models (SVM, Gradient Boosting, Neural Networks)
- Cross-validation for robust evaluation
- Feature importance analysis
- Deployment as a web application

## Author

**Khaja Masthan Shaik** (rexter001)

## License

This project is open source and available under the MIT License.
