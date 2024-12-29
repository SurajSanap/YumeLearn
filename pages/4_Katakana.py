import streamlit as st
import os
import json
from streamlit_lottie import st_lottie

from Home import load_animation

# Directories for Katakana images and audio
KATAKANA_IMAGE_DIR = "data/Katakana/Background"
KATAKANA_AUDIO_DIR = "data/Audio"



#st.set_page_config(page_title="YumeLearn", page_icon="assets/jp9.gif", layout="wide", initial_sidebar_state="expanded")

def render_katakana_page():
    st.title("Katakana Practice")
    st.markdown("Click on any Katakana character below to learn more about it!")

    # Display Katakana grid
    if os.path.exists(KATAKANA_IMAGE_DIR):
        images = [img for img in sorted(os.listdir(KATAKANA_IMAGE_DIR)) if img.endswith(".png")]
        cols = st.columns(5)
        for idx, img in enumerate(images):
            with cols[idx % 5]:
                if st.button(img.split(".")[0]):
                    show_modal(img)
    else:
        st.error("Katakana images not found.")

    # Sidebar with Lottie animation
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

def show_modal(img_name):
    """Displays a modal with a larger image and plays audio if available."""
    # Display the image
    img_path = os.path.join(KATAKANA_IMAGE_DIR, img_name)
    st.image(img_path, caption=img_name.split(".")[0])

    # Play corresponding audio if it exists
    audio_file = os.path.join(KATAKANA_AUDIO_DIR, f"{img_name.split('.')[0]}.mp3")
    if os.path.exists(audio_file):
        st.audio(audio_file)
    else:
        st.warning("Audio for this character is not available.")

    st.markdown("### Pronunciation and Stroke Animation Coming Soon!")

# Render the Katakana page
render_katakana_page()
