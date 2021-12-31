import streamlit as st

from apps.heartDisease import heartDisease
from apps.Diabetes_pred import diabetes

from multiapp import MultiApp

from apps import home
# import your app modules here
import time

app = MultiApp()


# Add all your application here
app.add_app("Home", home.app)

#Heart Disease APP calling app function
app.add_app("Heart Disease Detection",heartDisease.app)

#Diabetes APP calling app function
app.add_app("Diabetes Detection",diabetes.app)

with st.spinner("Getting things ready...."):
    # The main app
    app.run()
    time.sleep(5)

