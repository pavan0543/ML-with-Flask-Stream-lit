import numpy as np
import pickle
import pandas as pd
from flask import Flask, request

app=Flask(__name__)

pickle_in = open("linear_salarydata.pkl","rb")
classifier=pickle.load(pickle_in)


@app.route('/')      # decorator
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["Get"])
def predict_note_authentication():      


    input=['YearsExperience']
   
    list1=[]
    for i in input:
        val=request.args.get(i)
        list1.append(eval(val))
                     
    prediction=classifier.predict([list1])
    

    print(prediction)
    return "Hello The answer is"+str(prediction)
    
@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    df_test=pd.read_csv(request.files.get("file"))  
    prediction=classifier.predict(df_test)
    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)