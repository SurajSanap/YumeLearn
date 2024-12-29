import json
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="YumeLearn", page_icon="assets/jp9.gif", layout="wide", initial_sidebar_state="expanded")

def main():
    # Display title and welcome image
    st.title("Welcome to YumeLearn!")
    

    # Display animation using Lottie
    try:
        with open('assets/Animation.json', encoding='utf-8') as anim_source:
            animation_data = json.load(anim_source)
        st_lottie(animation_data, height=200, key="welcome_animation")
    except FileNotFoundError:
        st.error("Animation file not found.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Load the animation
animation_path = "assets/SakuraAnimation.json"
animation_data = load_animation(animation_path)

with st.sidebar:
    # Display Lottie animation instead of an image
    if animation_data:
        btn_face = "🌞" if st.session_state.get("current_theme", "light") == "light" else "🌜"
        if st.button(btn_face, key='unique_theme_toggle'):
            st.session_state["current_theme"] = "dark" if st.session_state.get("current_theme", "light") == "light" else "light"

        # tabs = st.radio(
        #     "Navigation",
        #     options=["Home", "Hiragana", "Katakana", "Kanji"],
        #     index=0,
        # )

        # menu = {
        #     "Home": lambda: st.write("Welcome to the Home Page!"),
        #     "Hiragana": lambda: st.write("Navigate to Hiragana Practice"),
        #     "Katakana": lambda: st.write("Navigate to Katakana Practice"),
        #     "Kanji": lambda: st.write("Navigate to Kanji Practice"),
        # }

        # if tabs in menu:
        #     menu[tabs]()

    # Footer
    st.markdown(
        """
        <footer style="position: fixed; bottom: 0; width: 100%; background-color: #2c2f33; color: white; text-align: center; padding: 10px;">
            © 2024 Suraj Sanap Project
        </footer>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("""
    This app helps you prepare for the **JLPT** (Japanese Language Proficiency Test) with:
    - Interactive Hiragana, Katakana, and Kanji practice.
    - Vocabulary and grammar lessons tailored to your JLPT level.
    - Listening comprehension exercises and mock tests.
    
    Start your journey today and achieve your language learning goals!
    """)
    st.image("assets/welcome_image.png", use_container_width=True)

if __name__ == "__main__":
    main()
