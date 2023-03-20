# -*- coding: utf-8 -*-
'''
@author: subhash g
'''

# -*- coding: utf-8 -*-
'''
@author: subhash g
'''





import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
from abalone_predictions import RandomForestClassifier
from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("RFC.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Length,Height,Whole_weight,Viscera_weight,Shell_weight,Sex_I,Sex_M):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    x=[[Length,Height,Whole_weight,Viscera_weight,Shell_weight,Sex_I,Sex_M]]
    prediction=classifier.predict(x)
    print(prediction)
    return prediction



def main():
    st.title(" Abalone_predictions")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Abalone_predictions ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Length = st.text_input("Length","Type Here")
    
   
    Height = st.text_input("Height","Type Here")
    
    Whole_weight = st.text_input("Whole_weight","Type Here")
    
    Viscera_weight = st.text_input("Viscera_weight","Type Here")
    
    Shell_weight = st.text_input("Shell_weight","Type Here")
    
    Sex_I = st.text_input("Sex_I","Type Here")

    Sex_M = st.text_input("Sex_M","Type Here")
    
   
    result=""
    if st.button("Predict"):
        Length=float(Length)
        Height=float(Height)
        Whole_weight=float(Whole_weight)
        Viscera_weight=float(Viscera_weight)
        Shell_weight=float(Shell_weight)
        Sex_I=float(Sex_I)
        Sex_M=float(Sex_M)
        
        result=predict_note_authentication(Length,Height,Whole_weight,Viscera_weight,Shell_weight,Sex_I,Sex_M)
    st.success('THE Abalone Age IS  {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    