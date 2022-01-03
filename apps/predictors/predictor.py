import streamlit as st
from apps.predictors.laptopPrice.laptopPrice import laptopMain

from apps.predictors.iplPredict.iplPredict import iplWin
def app():
    #home menu
    menu=["Laptop Price Predictor","Ipl Winner Probability Predictor"]

    choice = st.sidebar.selectbox("Different Analysis List",menu)

    ChoiceMenu(choice,menu)


def ChoiceMenu(choice,menu):
    if choice == menu[0]:
        laptopMain()
    
    elif choice == menu[1]:
        iplWin()
