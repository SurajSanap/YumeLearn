import json
import streamlit as st
from streamlit_lottie import st_lottie
import os
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="YumeLearn", page_icon="assets/jp9.png", layout="wide", initial_sidebar_state="expanded")

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

# Add CSS for animation and visibility
def add_custom_css():
    st.markdown("""
    <style>
    /* Smooth fade-in effect for the services section */
    #services {
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 1s ease-out, transform 1s ease-out;
    }
    #services.visible {
        opacity: 1;
        transform: translateY(0);
    }

    footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #332242;
        color: white;
        text-align: center;
        padding: 10px;
        z-index: 10;
    }

    .spacing {
        height: 200px;
    }
    </style>
    """, unsafe_allow_html=True)

# Add JavaScript to handle scroll-based visibility
def add_custom_js():
    components.html("""
    <script>
    document.addEventListener('scroll', function() {
        const services = document.getElementById('services');
        const rect = services.getBoundingClientRect();
        if (rect.top <= window.innerHeight && rect.bottom >= 0) {
            services.classList.add('visible');
        }
    });
    </script>
    """, height=0)

# Main function
def main():
    add_custom_css()
    add_custom_js()

    # Display Lottie animation for welcome
    animation_data = load_animation("assets/Animation.json")
    if animation_data:
        st_lottie(animation_data, height=200, key="welcome_animation_main")

    # Center-aligned title using columns
    col1, col2, col3 = st.columns([1, 6, 1])  # Adjust column width ratios
    with col2:  # Center column
        logo_path = os.path.join("assets", "YumeLeran Logo.png")
        if os.path.exists(logo_path):
            st.image(logo_path)
        else:
            st.error(f"Logo not found: {logo_path}")

    # Add spacing between logo and services
    st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)
    # Services Section
    st.write("<h1><center>Our Services</center></h1>", unsafe_allow_html=True)

    # Define services
    services = [
        {"name": "Hiragana Practice", "image": "assets/jp6.jpg", "description": "Learn and practice Hiragana characters interactively."},
        {"name": "Katakana Practice", "image": "assets/jp3.jpg", "description": "Master Katakana with guided lessons and exercises."},
        {"name": "Kanji Learning", "image": "assets/jp7.jpg", "description": "Understand and practice Kanji characters by levels."},
        {"name": "Tests and Quizzes", "image": "assets/jp5.jpg", "description": "Challenge yourself with Japanese language tests."},
    ]
    
    # Display services in a grid
    cols = st.columns(len(services))  # Create equal columns for each service
    for i, service in enumerate(services):
        with cols[i]:
            # Display image for the service
            if os.path.exists(service["image"]):
                st.image(service["image"], use_container_width=True, caption=service["name"])
            else:
                st.error(f"Image not found: {service['image']}")
            
            # Display service description
            st.markdown(service["description"])
    
    st.markdown("</div>", unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        # Load and display Lottie animation in sidebar
        sidebar_animation = load_animation("assets/SakuraAnimation.json")
        if sidebar_animation:
            st_lottie(sidebar_animation, height=80, key="sidebar_animation_sidebar")

        # Theme toggle button
        btn_face = "🌞" if st.session_state.get("current_theme", "light") == "light" else "🌜"
        if st.button(btn_face, key='unique_theme_toggle'):
            st.session_state["current_theme"] = "dark" if st.session_state.get("current_theme", "light") == "light" else "light"

        st.divider()

        # Sidebar information
        st.markdown("""
        ## About YumeLearn
        This app provides tools to master the Japanese language through:
        - Interactive practice with Hiragana, Katakana, and Kanji.
        - Vocabulary and grammar lessons designed to improve your language skills.
        - Exercises to enhance listening comprehension and overall proficiency.
        
        Embark on your language-learning adventure today!
        """)

    st.markdown("<div class='spacing'></div>", unsafe_allow_html=True)




    # Powered by section
    st.write("<h1><center>Powered by</center></h1>", unsafe_allow_html=True)
   
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("assets/GoogleGeminiLogo.png", caption="Google Gemini", width=200)
    with col2:
        st.image("assets/OpenAiLogo.png", caption="OpenAI", width=200)

    # Footer
    st.markdown(
        """
        <footer>
            © 2025 YumeLearn Project
        </footer>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
