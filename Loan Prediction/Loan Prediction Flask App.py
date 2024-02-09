import numpy as np
import pandas as pd
from flask import Flask,request
import warnings
warnings.filterwarnings("ignore")
import pickle


app = Flask(__name__)

pickle_in = open("Loan_prediction.pkl","rb")
classifier = pickle.load(pickle_in)

@app.route("/")
def welcome():
    return "Welcome All"

@app.route("/predict")
def prediction():

    input_cols = ['Loan_ID', 'Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']
    
    list1 = []

    for i in input_cols:
        val = request.args.get(i)
        list1.append(eval(val))

    print(list1)

    prediction =  classifier.predict([list1])

    print(prediction)

    return "The prediction value for loan status is : "+ str(prediction)


if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = 8000)
