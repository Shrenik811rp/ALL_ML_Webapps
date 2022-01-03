import streamlit as st

# importing different project modules
from apps.healthcare import healthCare
from apps.nlp import nlp
from apps.predictors import predictor

from multiapp import MultiApp

from apps import home
# import your app modules here
import time

app = MultiApp()


# Add all your application here
app.add_app("Home", home.app)

#Health Care APP calling app function
app.add_app("Health Care Prediction",healthCare.app)


#nlp projects
app.add_app("NLP Projects",nlp.app)

#predictor projects
app.add_app("Predictor Projects",predictor.app)



with st.spinner("Getting things ready...."):
    # The main app
    app.run()
    time.sleep(5)

