import streamlit as st

from apps.healthcare.heartDisease.heartDisease import Heartapp
from apps.healthcare.Diabetes_pred.diabetes import Diabapp

def app():
    #home menu
    menu=["Diabetes Analysis","Heart Disease Analysis"]

    choice = st.sidebar.selectbox("Different Analysis List",menu)

    ChoiceMenu(choice,menu)


def ChoiceMenu(choice,menu):
    if choice == menu[0]:
        Diabapp()
    
    elif choice == menu[1]:
        Heartapp()
