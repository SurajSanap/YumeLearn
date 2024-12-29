import json
import streamlit as st
from streamlit_lottie import st_lottie

# Set page configuration
st.set_page_config(page_title="YumeLearn", page_icon="assets/jp9.gif", layout="wide", initial_sidebar_state="expanded")

# Function to load Lottie animations
def load_animation(file_path):
    try:
        with open(file_path, encoding='utf-8') as anim_source:
            return json.load(anim_source)
    except FileNotFoundError:
        st.error(f"Animation file not found: {file_path}")
    except json.JSONDecodeError as e:
        st.error(f"Error decoding JSON: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
    return None

# Main function
def main():
    # Display title
    st.title("Welcome to YumeLearn!")

    # Display Lottie animation for welcome
    animation_data = load_animation("assets/Animation.json")
    if animation_data:
        st_lottie(animation_data, height=200, key="welcome_animation")

    # Sidebar
    with st.sidebar:
        # Load and display Lottie animation in sidebar
        sidebar_animation = load_animation("assets/SakuraAnimation.json")
        if sidebar_animation:
            st_lottie(sidebar_animation, height=80, key="sidebar_animation")

        # Theme toggle button
        btn_face = "🌞" if st.session_state.get("current_theme", "light") == "light" else "🌜"
        if st.button(btn_face, key='unique_theme_toggle'):
            st.session_state["current_theme"] = "dark" if st.session_state.get("current_theme", "light") == "light" else "light"

        # Sidebar information
        st.markdown("""
        ## About YumeLearn
        This app provides tools to master the Japanese language through:
        - Interactive practice with Hiragana, Katakana, and Kanji.
        - Vocabulary and grammar lessons designed to improve your language skills.
        - Exercises to enhance listening comprehension and overall proficiency.
        
        Embark on your language-learning adventure today!
    
        """)

    # Footer
    st.markdown(
        """
        <footer style="position: fixed; bottom: 0; width: 100%; background-color: #2c2f33; color: white; text-align: center; padding: 10px;">
            © 2024 Suraj Sanap Project
        </footer>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
