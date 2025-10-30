import streamlit as st
import pandas as pd

# Use wide layout for better image display
st.set_page_config(layout="wide")

st.write("Displaying bear data from a CSV, now with images! 🐻🖼️")

# Base URL for the images
IMAGE_BASE_URL = "https://raw.githubusercontent.com/dataprofessor/bear-dataset/refs/heads/master/images/"

# Load data from the provided URL
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/dataprofessor/bear-dataset/refs/heads/master/bear_data.csv"
    df = pd.read_csv(url)
    # Create a new column with the full, absolute image URL
    df['Image'] = IMAGE_BASE_URL + df['Image URL']
    return df

data = load_data()

# Configure the 'Image' column to be displayed as an image
# and hide the original 'Image URL' column
column_config = {
    "Image": st.column_config.ImageColumn(width="medium"),
    "Image URL": None 
}

# Display the data with an editing toggle
if st.toggle("Enable editing"):
    st.data_editor(
        data,
        column_config=column_config,
        use_container_width=True,
        hide_index=True,
    )
else:
    st.dataframe(
        data,
        column_config=column_config,
        use_container_width=True,
        hide_index=True,
    )

