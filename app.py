import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load Trained Model
# -----------------------------
model = joblib.load("model.pkl")

st.set_page_config(page_title="Loan Risk Prediction", layout="centered")

st.title("💳 Loan Default Prediction System")
st.markdown("""
This application predicts whether a loan applicant is likely to **Default** or **Repay**
based on financial and credit information.
""")

st.subheader(" Enter Applicant Details")

# -----------------------------
# User Inputs
# -----------------------------

age = st.number_input("Age", min_value=18, max_value=100)
income = st.number_input("Annual Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
credit_history = st.number_input("Credit History Length (Years)", min_value=0)

previous_default = st.selectbox(
    "Previously Defaulted?",
    ["No", "Yes"]
)

loan_grade = st.selectbox(
    "Loan Grade",
    ["A", "B", "C", "D", "E", "F", "G"]
)

# -----------------------------
# Prediction Button
# -----------------------------

if st.button(" Predict Risk"):

    # Get model expected feature names
    expected_columns = model.feature_names_in_

    # Create dictionary with all features initialized to 0
    input_data = {col: 0 for col in expected_columns}

    # Map numerical features
    if "person_age" in expected_columns:
        input_data["person_age"] = age

    if "person_income" in expected_columns:
        input_data["person_income"] = income

    if "loan_amnt" in expected_columns:
        input_data["loan_amnt"] = loan_amount

    if "cb_person_cred_hist_length" in expected_columns:
        input_data["cb_person_cred_hist_length"] = credit_history

    # Encode previous default
    if previous_default == "Yes":
        col_name = "cb_person_default_on_file_Y"
        if col_name in expected_columns:
            input_data[col_name] = 1

    # Encode loan grade
    grade_column = f"loan_grade_{loan_grade}"
    if grade_column in expected_columns:
        input_data[grade_column] = 1

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # Predict
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.subheader("📊 Prediction Result")

    if prediction == 1:
        st.error("❌ High Risk: Loan likely to DEFAULT")
    else:
        st.success("✅ Low Risk: Loan likely to be REPAID")

    st.write(f"Default Probability: {round(probability*100,2)}%")

# -----------------------------
# Footer
# -----------------------------

st.markdown("---")
st.caption("End-to-End Machine Learning Model Deployment with Streamlit")