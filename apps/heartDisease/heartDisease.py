
#importing eda module for heart disease
from apps.heartDisease.eda import eda

from apps.heartDisease.ml import ml


#importing required general modules
import streamlit as st
import pandas as pd
import time

#main app function
def app():
    
    #home menu
    menu=["Heart Disease Home","Exploratory Data Analysis Section", "Prediction Section","About"]

    choice = st.sidebar.selectbox("Menu",menu)

    ChoiceMenu(choice)



#choice selection function
def ChoiceMenu(choice):


    #calling required function based on user input
    if choice == "Heart Disease Home":

        #display info on home page
        st.title('Heart Disease App')
        st.header("Heart Disease Home Page")


    elif choice == "Exploratory Data Analysis Section":

        #display eda info
        st.header("Exploratory Data Analysis Section") 

        #calling main eda module 
        eda()


    elif choice == "Prediction Section":

        #display model predictions
        st.header("Prediction Section") 
        ml() 


    else:
        st.header("About Page") 
    
