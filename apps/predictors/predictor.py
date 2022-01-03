import streamlit as st
from apps.predictors.laptopPrice.laptopPrice import laptopMain

def app():
    #home menu
    menu=["Laptop Price Predictor","Employer Salary Predictor"]

    choice = st.sidebar.selectbox("Different Analysis List",menu)

    ChoiceMenu(choice,menu)


def ChoiceMenu(choice,menu):
    if choice == menu[0]:
        laptopMain()
    
    elif choice == menu[1]:
        pass
