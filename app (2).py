import streamlit as st
import numpy as np
import pickle
import math
from flask import Flask, request, jsonify, render_template 

app = Flask(__name__, template_folder="template", static_folder="staticfiles")
model = pickle.load(open('build.pkl', "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        int_features = [int(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        
        if prediction == 1:
            return render_template('index.html', prediction_text="Loan is Rejected")
        else:
            return render_template('index.html', prediction_text="Loan is Approved")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
