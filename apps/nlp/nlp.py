import streamlit as st


def app():
    #home menu
    menu=["Text Summary","Emotion Analysis"]

    choice = st.sidebar.selectbox("Different Analysis List",menu)

    ChoiceMenu(choice,menu)


def ChoiceMenu(choice,menu):
    if choice == menu[0]:
        pass
    
    elif choice == menu[1]:
        pass
