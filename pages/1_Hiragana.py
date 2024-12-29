import streamlit as st
import os

# Directories for Hiragana images and audio
HIRAGANA_IMAGE_DIR = "data/Hiragana/Background"
HIRAGANA_AUDIO_DIR = "data/Audio"

st.set_page_config(page_title="YumeLearn", page_icon="assets/jp9.gif", layout="wide", initial_sidebar_state="expanded")


def render_hiragana_page():
    st.title("Hiragana Practice")
    st.markdown("Click on any Hiragana character below to learn more about it!")

    # Display Hiragana grid
    if os.path.exists(HIRAGANA_IMAGE_DIR):
        images = [img for img in sorted(os.listdir(HIRAGANA_IMAGE_DIR)) if img.endswith(".png")]
        cols = st.columns(5)
        for idx, img in enumerate(images):
            with cols[idx % 5]:
                if st.button(img.split(".")[0]):
                    show_modal(img)
    else:
        st.error("Hiragana images not found.")

def show_modal(img_name):
    """Displays a modal with a larger image and plays audio if available."""
    # Display the image
    img_path = os.path.join(HIRAGANA_IMAGE_DIR, img_name)
    st.image(img_path, caption=img_name.split(".")[0])

    # Play corresponding audio if it exists
    audio_file = os.path.join(HIRAGANA_AUDIO_DIR, f"{img_name.split('.')[0]}.mp3")
    if os.path.exists(audio_file):
        st.audio(audio_file)
    else:
        st.warning("Audio for this character is not available.")

    st.markdown("")

    st.markdown(
        """
        <footer style="position: fixed; bottom: 0; width: 100%; background-color: #2c2f33; color: white; text-align: center; padding: st.query_params;">
            © 2024 YumeLearn Project
        </footer>
        """,
        unsafe_allow_html=True,
    )

# Render the Hiragana page
render_hiragana_page()
