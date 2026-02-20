# 💳 Loan Default Prediction System

An end-to-end Machine Learning project that predicts whether a loan applicant is likely to Default or Repay based on financial and credit information.

This project demonstrates a complete Data Science workflow including data preprocessing, exploratory data analysis (EDA), feature engineering, model comparison, evaluation, and deployment using Streamlit.

---

## 🚀 Project Overview

Financial institutions face significant losses due to loan defaults.  
This project builds a classification model that predicts loan risk using applicant financial and credit history features.

The deployed system provides:

- ✅ Low Risk (Likely to Repay)
- ❌ High Risk (Likely to Default)
- 📊 Default Probability (%)

---

## 📊 Dataset

Credit Risk Dataset containing features such as:

- Age
- Annual Income
- Loan Amount
- Credit History Length
- Previous Default History
- Loan Grade

---

## 🧠 Machine Learning Models Used

Three models were trained and compared:

1. Logistic Regression  
2. Random Forest  
3. XGBoost  

### 📈 Model Performance Summary

| Model                | Accuracy | Recall (Default) | F1 Score |
|----------------------|----------|------------------|----------|
| Logistic Regression  | 78%      | 60%              | 0.54     |
| Random Forest        | 92%      | 74%              | 0.80     |
| XGBoost              | 93%      | 74%              | 0.83     |

### ✅ Final Model Selected: XGBoost

Reason:
- Higher F1 Score
- Strong Recall for Default class
- Better balance between Precision and Recall
- Better generalization performance

Since loan default detection is risk-sensitive, Recall and F1-score were prioritized over simple Accuracy.

---

## 📈 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Default Probability

Special focus was given to reducing False Negatives (missing risky customers).

---

## 🖥️ Streamlit Deployment

The final model was deployed using Streamlit to create an interactive web application.

### Features of Web App:

- User input form
- Real-time prediction
- Default probability display
- Risk classification (Low / High)
- Clean UI design
- Feature alignment handling

---

## 📂 Project Structure

Loan_Default_Project/

- app.py
- model.pkl
- requirements.txt
- notebooks/
- data/
- dashboard/
- doc/
- README.md

---

## ⚙️ How to Run Locally

1️⃣ Clone the repository:

git clone https://github.com/yourusername/Loan-Default-Prediction.git  
cd Loan-Default-Prediction  

2️⃣ Install dependencies:

pip install -r requirements.txt  

3️⃣ Run the Streamlit app:

streamlit run app.py  

Open in browser:

http://localhost:8501  

---

## 🔧 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Streamlit
- Git & GitHub

---

## 📌 Key Learning Outcomes

- Handling class imbalance
- Feature encoding and alignment
- Model comparison strategy
- Confusion matrix interpretation
- Probability-based classification
- Model deployment using Streamlit
- Debugging environment and dependency issues

---

## 🎯 Future Improvements

- Hyperparameter tuning
- SHAP explainability integration
- CI/CD automation
- Cloud deployment
- Model monitoring system

---

## 👩‍💻 Author

Honey Upadhyay  
B.Tech (Computer Science)  
Data Science & Machine Learning Enthusiast  

---

