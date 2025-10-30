import streamlit as st
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/bear-dataset/refs/heads/master/bear_data.csv")
st.dataframe(df)
