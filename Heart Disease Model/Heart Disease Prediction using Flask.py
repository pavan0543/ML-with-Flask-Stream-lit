import pickle
import pandas as pd 
import numpy as np 
from flask import Flask , request
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

pickle_in = open("Heart Disease Analysis.pkl","rb")
classifier = pickle.load(pickle_in)

@app.route("/")
def welcome():
    return "Welcome To All"

@app.route("/predict",methods = ["GET"])
def prediction_note():

    input_cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal']
    
    list1 = []

    for i in input_cols:
        value = request.args.get(i)
        list1.append(eval(value))
    print(list1)
    
   # input_data = np.array(list1).reshape(1, -1)

    prediction = classifier.predict([list1])

    print(prediction)
    return "Hello The Predicted value is : "+str(prediction)


@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    df_test=pd.read_csv(request.files.get("file"))  # whatever name you written here the same name will provide in Post man
    prediction=classifier.predict(df_test)
    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
