

#importing general libraries
from seaborn.axisgrid import pairplot
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

import matplotlib.pyplot as plt



#eda main function
def eda():

    #read dataset file
    df = pd.read_csv("datasets/heart.csv")
    EdaChoice(df)
    

# choose the sub menu in eda section
def EdaChoice(df):

    #setting a submenu for eda part
    submenu = ["Descriptive","Plots"]

    #getting user input for choice
    choice = st.sidebar.selectbox("Sub-Menu",submenu)


    if choice == "Descriptive":
        EdaDes(df)    

    else:
        EdaPlot(df)



def EdaDes(df):
    st.subheader("Heart Dataset")
    st.dataframe(df)

    st.subheader("Statistics")
    with st.expander("General Statistics:"):
        st.dataframe(df.describe())
    EdaDesClean(df)
    

def genderReplace(df):
    df['sex'].replace(0, 'Female',  inplace=True)
    df['sex'].replace(1, 'Male',    inplace=True)
    return df

def ecgReplace(df):
    df['restecg'].replace(1, 'ST-T wave abnormality',  inplace=True)
    df['restecg'].replace(0, 'Normal',    inplace=True)
    df['restecg'].replace(2, 'Left ventricular hypertrophy ',    inplace=True)
    return df

def chestReplace(df):
    df['cp'].replace(0, 'Typical Angina',  inplace=True)
    df['cp'].replace(1, 'Atypical angina',    inplace=True)
    df['cp'].replace(2, 'Non-Anginal Pain',  inplace=True)
    df['cp'].replace(3, 'Asymtomatic',    inplace=True)

    return df

def bpSugarReplace(df):
    df['fbs'].replace(1, 'True',  inplace=True)
    df['fbs'].replace(0, 'False',    inplace=True)

    return df

def targetReplace(df):
    # Replace 0 and 1 with yes and no
    df['target'].replace(0, 'No',  inplace=True)
    df['target'].replace(1, 'Yes',    inplace=True)

    return df

def exangReplace(df):
    # replace exang with Yes and No
    df['exang'].replace(0, 'No',  inplace=True)
    df['exang'].replace(1, 'Yes',    inplace=True)
    return df



def EdaDesClean(df):

    col1,col2 = st.columns(2)

    with col1:

        with st.expander("Gender Count"):
            df = genderReplace(df)
            st.write(df["sex"].value_counts())
        
        with st.expander("Resting ECG"):

            df = ecgReplace(df)
            st.write(df["restecg"].value_counts())

    with col2:

        with st.expander("Chest Pain Type"):
            df = chestReplace(df)
            st.write(df["cp"].value_counts())
        
        with st.expander("Fasting Blood Sugar"):
            
            df = bpSugarReplace(df)
            st.write(df["fbs"].value_counts())



def EdaPlot(df):
    with st.expander("Based on Column Target"):

        targetList = ["Target","Target wrt Sex","Target wrt Fasting Blood Sugar","Target wrt Exercise Infused Angina"]
        choose = st.selectbox("Choose plot type:",targetList)


        if choose == targetList[0]:

            df = targetReplace(df)
            #dispaying relavent plot based on target
            plotTarget = px.histogram(df,x="target",nbins=10,color="target")
            st.plotly_chart(plotTarget)

        
        elif choose == targetList[1]:

            df = genderReplace(df)
            plotTargetSex = px.histogram(df,x="target",nbins=10,color="sex",barmode="group")
            st.plotly_chart(plotTargetSex)

        elif choose == targetList[2]:
            df = bpSugarReplace(df)
            plotTargetFbs = px.histogram(df,x="target",nbins=10,color="fbs")
            st.plotly_chart(plotTargetFbs)

        else:
            df = exangReplace(df)
            plotTargetAngina = px.histogram(df,x="target",nbins=10,color="exang",barmode="group")
            st.plotly_chart(plotTargetAngina)
        

    with st.expander("Frequency Distribution Plot"):

        freqList = ["Plot Based on Chest Pain","Plot Based on Max Heart Rate","Plot Based on Age"]
        choose = st.selectbox("Choose Frequency Plot:",freqList)


        if choose == freqList[0]:

            df = chestReplace(df)
            plotPieChest = px.pie(df,names="cp")
            st.plotly_chart(plotPieChest)

        
        elif choose == freqList[1]:

            figureMaxHeart ,axisMaxHeart = plt.subplots(figsize=(10,8))

            axisMaxHeart = sns.distplot(df["thalach"],bins=10)
            st.pyplot(figureMaxHeart)

        else:
            
            figureAgePlot ,axisAgePlot = plt.subplots(figsize=(10,8))

            axisAgePlot = sns.distplot(df["age"],bins=10,color="red")
            st.pyplot(figureAgePlot)



    with st.expander("Scatter Plots"):

        scatterList = ["Age VS Resting Blood Pressure","Age VS Cholestrol","Cholestrol VS Maximum Heart Rate"]
        choose = st.selectbox("Choose plot type:",scatterList)


        if choose == scatterList[0]:
            ageRestBP , ageRestBPAxis = plt.subplots(figsize=(10,8))
            ageRestBPAxis = sns.scatterplot(x="age",y="trestbps",data=df)
            st.pyplot(ageRestBP)


        elif choose == scatterList[1]:
            ageCholestrol , ageCholAxis = plt.subplots(figsize=(10,8))
            ageCholAxis = sns.scatterplot(x="age",y="chol",data=df)
            st.pyplot(ageCholestrol)

        
        else:
            CholHeartRate , CholHeartRateAxis = plt.subplots(figsize=(10,8))
            CholHeartRateAxis = sns.scatterplot(x="chol",y="thalach",data=df)
            st.pyplot(CholHeartRate)

        

    with st.expander("Outlier Detection"):
        outlierList = ["Age","Resting Blood Pressure","Cholestrol","Maximum Heart Rate"]
        choose = st.selectbox("Choose plot type:",outlierList)

        if choose == outlierList[0]:
            AgeOutlier = px.box(df,x="age")
            st.plotly_chart(AgeOutlier)

        elif choose == outlierList[1]:
            RestBPOutlier = px.box(df,x="trestbps")
            st.plotly_chart(RestBPOutlier)
        
        elif choose == outlierList[2]:
            CholOutlier = px.box(df,x="chol")
            st.plotly_chart(CholOutlier)
        
        else:
            MaxHeartOutlier = px.box(df,x="thalach")
            st.plotly_chart(MaxHeartOutlier)


    with st.expander("HeatMaps and Pairplots"):
        choose = st.selectbox("Choose plot type:",["Heat-Maps","Pair-Plots"])

        if choose == "Heat-Maps":
            heatMap = df.corr()
            heatPlot = px.imshow(heatMap)

            st.plotly_chart(heatPlot)

        else:
            pairPlot = plt.figure()
            sns.pairplot(pairplot)
            st.pyplot(pairplot)