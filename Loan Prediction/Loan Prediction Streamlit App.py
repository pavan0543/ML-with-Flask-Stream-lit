import streamlit as st
import numpy as np
import pandas as pd
import pickle
import warnings
warnings.filterwarnings("ignore")


pickle_in = open("Loan_prediction.pkl","rb")
classifier = pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note(Loan_ID, Gender, Married, Dependents, Education,
       Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount,
       Loan_Amount_Term, Credit_History, Property_Area):
    
    prediction = classifier.predict([[Loan_ID, Gender, Married, Dependents, Education,
       Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount,
       Loan_Amount_Term, Credit_History, Property_Area]])
    
    print(prediction)

    return "The Loan Prediction status is : " + str(prediction)

def main():
    st.title("Loan Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Loan Prediction Status ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    Loan_ID = st.text_input("Loan ID")
    Gender = st.text_input("Gender")
    Married = st.text_input("Married")
    Dependents = st.text_input("Dependents")
    Education = st.text_input("Education")
    Self_Employed = st.text_input("Self_Employed")
    ApplicantIncome = st.text_input("Applicant Income")
    CoapplicantIncome = st.text_input("Cpapplicant Income")
    LoanAmount = st.text_input("Loan Amount")
    Loan_Amount_Term = st.text_input("Loan Amount Term")
    Credit_History = st.text_input("Credit History")
    Property_Area = st.text_input("Property Area")
    result = ""

    if st.button("Predict"):
        result = predict_note(eval(Loan_ID), eval(Gender), eval(Married), eval(Dependents), eval(Education),
       eval(Self_Employed), eval(ApplicantIncome), eval(CoapplicantIncome), eval(LoanAmount),
       eval(Loan_Amount_Term), eval(Credit_History), eval(Property_Area))
    st.success("The Loan Status is : {}".format(result))
    if st.button("About"):
        st.text("Lets Learn ")
        st.text("It is abount Loan Prediction ")

if __name__ == "__main__":
    main()