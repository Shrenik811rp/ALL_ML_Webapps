


#importing general libraries
from seaborn.axisgrid import pairplot
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def eda():
    df = pd.read_csv("datasets/diabetes.csv")

    edaChoice(df)



def edaChoice(df):
     #setting a submenu for eda part
    submenu = ["Descriptive","Plots"]

    #getting user input for choice
    choice = st.sidebar.selectbox("Sub-Menu",submenu)


    if choice == submenu[0]:
        EdaDiabDes(df)    

    else:
        EdaDiabPlot(df)


'''
Function to clean NaN values
'''

def cleanData(df):
    
    df_copy = df.copy(deep = True)
    df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)
    df_copy['Glucose'].fillna(df_copy['Glucose'].mean(), inplace = True)
    df_copy['BloodPressure'].fillna(df_copy['BloodPressure'].mean(), inplace = True)
    df_copy['SkinThickness'].fillna(df_copy['SkinThickness'].median(), inplace = True)
    df_copy['Insulin'].fillna(df_copy['Insulin'].median(), inplace = True)
    df_copy['BMI'].fillna(df_copy['BMI'].median(), inplace = True)

    return df



def EdaDiabDes(df):
    st.subheader("Diabetes Dataset")
    st.dataframe(df)

    st.subheader("Statistics")
    with st.expander("General Statistics:"):
        st.dataframe(df.describe().T)
    with st.expander("Columns:"):
        st.dataframe(df.columns.T)




def EdaDiabPlot(df):
    
    with st.expander("Histogram Plots"):
        diabPlot = ["Age","BMI","BloodPressure","Insulin","Pregnancies"]

        choose = st.selectbox("Choose feature to plot",diabPlot)

        df = cleanData(df)

        if choose == diabPlot[0]:
            plotAge = px.histogram(df,x="Age",nbins=5,color="Age")
            st.plotly_chart(plotAge)
        
        elif choose == diabPlot[1]:
            plotBMI =  px.histogram(df,x="BMI",nbins=5,color="BMI")
            st.plotly_chart(plotBMI)
        elif choose == diabPlot[2]:
            plotBP =  px.histogram(df,x="BloodPressure",nbins=5,color="BloodPressure")
            st.plotly_chart(plotBP)
        elif choose == diabPlot[3]:
            plotInsulin =  px.histogram(df,x="Insulin",nbins=5,color="Insulin")
            st.plotly_chart(plotInsulin)
        else:
            plotPregnancies =  px.histogram(df,x="Pregnancies",nbins=5,color="Pregnancies")
            st.plotly_chart(plotPregnancies)



# def EdaDes(df):


#     col1,col2 = st.columns(2)

#     with col1:

#         with st.expander(""):
#             df = genderReplace(df)
#             st.write(df["sex"].value_counts())
        
#         with st.expander("Resting ECG"):

#             df = ecgReplace(df)
#             st.write(df["restecg"].value_counts())

#     with col2:

#         with st.expander("Chest Pain Type"):
#             df = chestReplace(df)
#             st.write(df["cp"].value_counts())
        
#         with st.expander("Fasting Blood Sugar"):
            
#             df = bpSugarReplace(df)
#             st.write(df["fbs"].value_counts())