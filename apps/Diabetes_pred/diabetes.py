#importing eda module for heart disease
from apps.Diabetes_pred.edaDiab import eda

from apps.Diabetes_pred.mlDiab import ml


#importing required general modules
import streamlit as st
import pandas as pd
import time



def app():
    #home menu
    menu=["Diabetes Home","Exploratory Data Analysis Section", "Prediction Section","About"]

    choice = st.sidebar.selectbox("Menu",menu)

    ChoiceMenu(choice,menu)


#choice selection function
def ChoiceMenu(choice,menu):


    #calling required function based on user input
    if choice == menu[0]:

        #display info on home page
        st.title('Diabetes Prediction App')
        st.header("Diabetes Home Page")


    elif choice == menu[1]:

        #display eda info
        st.header("Exploratory Data Analysis Section") 

        #calling main eda module 
        eda()


    elif choice == menu[2]:

        #display model predictions
        st.header("Prediction Section") 
        st.subheader("Please enter patient data:")
        ml() 


    else:
        st.header("About Page") 
    
