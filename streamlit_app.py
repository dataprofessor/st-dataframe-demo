import streamlit as st
import pandas as pd

# Use wide layout for better image display
st.set_page_config(layout="wide")

# Load data from provided URL
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/bear-dataset/refs/heads/master/bear_data.csv")
    IMAGE_BASE_URL = "https://raw.githubusercontent.com/dataprofessor/bear-dataset/refs/heads/master/images/"
    df['images'] = IMAGE_BASE_URL + df['id'] + '.png'
    return df

# Display the URL as an image
column_config = {
    "images": st.column_config.ImageColumn("Image", width="small"),
    "Image": None
}

# Display the dataframe
data = load_data()
st.dataframe(
        data,
        column_config=column_config,
        use_container_width=True,
        hide_index=True,
    )
