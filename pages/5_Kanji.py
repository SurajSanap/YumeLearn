import streamlit as st
import os
import json
from streamlit_lottie import st_lottie

from Home import load_animation

st.set_page_config(page_title="YumeLearn", page_icon="assets/jp9.gif", layout="wide", initial_sidebar_state="expanded")

# Updated Kanji directories for different JLPT levels
KANJI_DIRS = {
    "JLPT-N5": "data/kanji/JLPT-N5",
    "JLPT-N4": "data/kanji/JLPT-N4",
    "JLPT-N3": "data/kanji/JLPT-N3",
}

# Initialize session state for the selected Kanji
if "selected_kanji" not in st.session_state:
    st.session_state.selected_kanji = None
if "selected_level" not in st.session_state:
    st.session_state.selected_level = None

def render_kanji_page():
    st.title("Kanji Practice")
    st.markdown("Select a JLPT level and click on any Kanji to view its details!")

    # JLPT Level Selection
    level = st.selectbox("Select JLPT Level", list(KANJI_DIRS.keys()))
    st.session_state.selected_level = level

    # Display Kanji table or full-size image based on the state
    if st.session_state.selected_kanji:
        display_kanji_image()
    else:
        # Display Kanji table for the selected level
        if level in KANJI_DIRS and os.path.exists(KANJI_DIRS[level]):
            kanji_images = [img for img in sorted(os.listdir(KANJI_DIRS[level])) if img.endswith(".png")]
            if kanji_images:
                kanji_table(kanji_images, KANJI_DIRS[level])
            else:
                st.warning("No Kanji images found for this level.")
        else:
            st.error("The selected JLPT level folder does not exist.")

    #Side bar
    with st.sidebar:
        sidebar_animation = load_animation("assets/SakuraAnimation.json")
        if sidebar_animation:
            st_lottie(sidebar_animation, height=150, key="sidebar_animation")

    
    st.markdown(
        """
        <footer style="position: fixed; bottom: 0; width: 100%; background-color: #2c2f33; color: white; text-align: center; padding: st.query_params;">
            © 2024 YumeLearn Project
        </footer>
        """,
        unsafe_allow_html=True,
    )

def kanji_table(kanji_images, folder_path):
    """Displays Kanji as a table and allows clicking to view details."""
    kanji_names = [img.split(".")[0] for img in kanji_images]
    cols = st.columns(5)  # Create a table with 5 columns

    for idx, kanji in enumerate(kanji_names):
        with cols[idx % 5]:
            if st.button(kanji, key=f"kanji_{kanji}"):  # Button for each Kanji
                # Update session state with the selected Kanji
                st.session_state.selected_kanji = {"name": kanji, "folder": folder_path}

def display_kanji_image():
    """Displays the selected Kanji image in full size."""
    selected_kanji = st.session_state.selected_kanji
    kanji_name = selected_kanji["name"]
    folder_path = selected_kanji["folder"]

    st.markdown(f"### Kanji: {kanji_name}")
    image_path = os.path.join(folder_path, f"{kanji_name}.png")
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)  # Display image in full width
    else:
        st.error(f"Image for {kanji_name} not found.")

    # Back button to return to Kanji table
    if st.button("Back to Kanji Practice"):
        st.session_state.selected_kanji = None



# Render the main Kanji Practice page
render_kanji_page()
