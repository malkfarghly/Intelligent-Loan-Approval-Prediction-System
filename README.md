# Intelligent Loan Approval Prediction System

## Overview
This project aims to predict loan approval decisions using Machine Learning techniques based on applicants’ financial, personal, and credit-related information.

The project workflow includes:
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Dimensionality Reduction
- Model Training
- Hyperparameter Tuning
- Model Evaluation

The final optimized Support Vector Machine (SVM) model achieved:
- Accuracy: 91.67%
- ROC-AUC Score: 0.9679

---

# Dataset Information

| Feature | Details |
|---|---|
| Dataset Size | 20,000 Records |
| Total Features | 35 Features |
| Target Variable | LoanApproved |

## Target Labels
- 1 → Approved
- 0 → Rejected

---

# Main Features Used
- Age
- AnnualIncome
- CreditScore
- EmploymentStatus
- EducationLevel
- LoanAmount
- DebtToIncomeRatio
- PaymentHistory
- BankruptcyHistory
- MonthlyIncome
- SavingsAccountBalance

---

# Data Cleaning

To prevent Data Leakage, the following columns were removed:
- RiskScore
- InterestRate
- BaseInterestRate
- MonthlyLoanPayment

## Additional Preprocessing Steps
- Missing Value Checking
- Outlier Detection using IQR
- Outlier Handling using Capping

---

# Exploratory Data Analysis (EDA)

EDA was performed to analyze:
- Loan approval distribution
- Credit score behavior
- Income distribution
- Employment status impact
- Bankruptcy history effect

## Key Insights
- Higher credit scores increase loan approval probability
- Higher annual income is associated with approved loans
- Bankruptcy history negatively affects loan approval decisions

---

# Preprocessing

## Encoding
- OrdinalEncoder

## Feature Scaling
- StandardScaler

## Pipeline Components
- ColumnTransformer
- Pipeline

---

# Dimensionality Reduction

Comparison between PCA and SelectKBest:

- PCA → 90.45% accuracy
- SelectKBest → 91.39% accuracy

Best Method:
- SelectKBest

---

# Machine Learning Model

## Model Used
- Support Vector Machine (SVM)

## Hyperparameter Tuning
- GridSearchCV
- StratifiedKFold

## Best Parameters
{
    'svm__C': 1,
    'svm__gamma': 'scale',
    'svm__kernel': 'linear'
}

---

# Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

# Final Results

- Accuracy: 91.67%
- ROC-AUC: 0.9679

---

# Conclusion
The project successfully demonstrated the effectiveness of Machine Learning techniques in predicting loan approval decisions.

Feature selection using SelectKBest improved model performance, while the optimized SVM model achieved strong accuracy and an excellent ROC-AUC score.

---

# Future Improvements
- Apply ensemble models such as Random Forest and XGBoost
- Add advanced feature engineering techniques to further improve performance
