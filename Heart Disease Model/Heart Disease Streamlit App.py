import pandas as pd
import numpy as np
import pickle 
import warnings
warnings.filterwarnings("ignore")
from flask import Flask, request

import streamlit as st

pickle_in = open("Heart Disease Analysis.pkl","rb")
classifier = pickle.load(pickle_in)

def welcome():
    return "Hi Welcome All"
def predict_note(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
   
    prediction=classifier.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    print(prediction)
    return prediction
    
    # input_cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
    #    'exang', 'oldpeak', 'slope', 'ca', 'thal']
    
    # list1 = []

    # for i in input_cols:
    #     value = request.args.get(i)
    #     list1.append(eval(value))
    # print(list1)
    

    # prediction = classifier.predict([list1])

    # print(prediction)
    # return "Hello The Predicted value is : "+str(prediction)

def main():
    st.title("Heart Disease Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Heart Disease Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("age","Type Here")
    sex = st.text_input("sex","Type Here")
    cp = st.text_input("cp","Type Here")
    trestbps = st.text_input("trestbps","Type Here")
    chol = st.text_input("chol","Type Here")
    fbs = st.text_input("fbs","Type Here")
    restecg = st.text_input("restecg","Type Here")
    thalach = st.text_input("thalach","Type Here")
    exang = st.text_input("exang","Type Here")
    oldpeak = st.text_input("oldpeak","Type Here")
    slope = st.text_input("slope","Type Here")
    ca = st.text_input("ca","Type Here")
    thal = st.text_input("thal","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note(eval(age), eval(sex), eval(cp), 
                                           eval(trestbps),eval(chol), eval(fbs), 
                                           eval(restecg), eval(thalach),
                                           eval(exang), eval(oldpeak), eval(slope),eval(ca),eval(thal))
        #result = predict_note()
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("This is about Heart Disease Analysis data")

if __name__=='__main__':
    main()
    