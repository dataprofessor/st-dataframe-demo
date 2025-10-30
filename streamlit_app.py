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
    # The original filename is in the 'Image' column
    df['full_image_url'] = IMAGE_BASE_URL + df['Image']
    return df

data = load_data()

# Configure the 'full_image_url' column to be displayed as an image
# and hide the original 'Image' column (which just has the filename)
column_config = {
    "full_image_url": st.column_config.ImageColumn("Image", width="medium"), # Display the full URL as an image
    "Image": None # Hide the original column with just the filename
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

