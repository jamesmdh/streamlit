import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    ["Overview", "EDA", "OCR", "Object Detection", "NLP", "Speech to Text"])

with tab1:
    st.title("Overiew")
    st.write("In this demo, I am creating a Streamlit app to explore various ML examples and showcase all that Streamlit has to offer!")

with tab2:
    st.title("Explotatory Data Analysis")
    #st.text("In this demo, I am creating a Streamlit app to analyze an ML example from Kaggle.")

    uploaded_file = st.file_uploader("Upload a CSV file here")

    if uploaded_file:

        st.header("Data Statistics")
        df = pd.read_csv(uploaded_file)
        #df['Year'] = df['Year'].astype('int64')
        st.write(df.describe())

        st.header("Data Header")
        st.write(df.head())

        #fig, ax = plt.subplots(1, 1)
        #ax.scatter(x=df['Year'], y=df['Global Sales Volume'])
        # ax.set_xlabel('Year')
        #ax.set_ylabel('Global Sales Volume')

with tab3:
    st.title("Optical Character Recognition (OCR)")

    png_uploaded_file = st.file_uploader("Upload a PNG file here")

    if png_uploaded_file:
        st.write("File uploaded!")

with tab4:
    st.title("Object Detection")

with tab5:
    st.title("Natural Language Processing (NLP)")

with tab6:
    st.title("Speech to Text")
