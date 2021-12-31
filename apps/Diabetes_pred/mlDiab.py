# Import our packages
import streamlit as st
import joblib
import os
import numpy as np
import pandas as pd
import plotly.figure_factory as ff
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split






# FUNCTION
def user_report():
  pregnancies = st.slider('Pregnancies', 0,17, 3 )
  glucose = st.number_input('Glucose', 0,200, 120 )
  bp = st.slider('Blood Pressure', 0,122, 70 )
  skinthickness = st.number_input('Skin Thickness', 0,100, 20 )
  insulin = st.slider('Insulin', 0,846, 79 )
  bmi = st.number_input('BMI', 0,67, 20 )
  dpf = st.slider('Diabetes Pedigree Function', 0.0,2.4, 0.47 )
  age = st.number_input('Age', 21,88, 33 )

  user_report_data = {
      'pregnancies':pregnancies,
      'glucose':glucose,
      'bp':bp,
      'skinthickness':skinthickness,
      'insulin':insulin,
      'bmi':bmi,
      'dpf':dpf,
      'age':age
  }
  report_data = pd.DataFrame(user_report_data, index=[0])
  return report_data



def ml():

    # X AND Y DATA
    df = pd.read_csv("datasets/diabetes.csv")
    x = df.drop(['Outcome'], axis = 1)
    y = df.iloc[:, -1]
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.33, random_state = 1000)


    # PATIENT DATA
    user_data = user_report()
    st.subheader('Patient Data')
    with st.expander("Input Patient Data:"):
        st.write(user_data)




    # MODEL
    rf  = RandomForestClassifier()
    rf.fit(x_train, y_train)
    user_result = rf.predict(user_data)



    # VISUALISATIONS
    st.subheader('Visualised Patient Report')

    # OUTPUT
    st.write('Your Report: ')
    output=''
    if user_result[0]==0:
        output = 'You are not Diabetic...'
        st.success(output)
    else:
        output = 'You are Diabetic... See a Doctor'
        st.warning(output)
    st.subheader('Accuracy Score: ')

    with st.expander("Final Accuracy:"):
        st.write(str(accuracy_score(y_test, rf.predict(x_test))*100)+'%')