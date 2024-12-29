import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm
from dotenv import load_dotenv
import os
import json
from streamlit_lottie import st_lottie

# Load environment variables
load_dotenv()

# Configure API Key
API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

def main():

    with open('assets/Teacher2.json', encoding='utf-8') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 200, -200)

    st.write("<h1><center>Japanese Teacher ChatBot</center></h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: center;'>Powered by google gemini</p>", unsafe_allow_html=True)

    # Load animation
  

    # Chatbot interface
    
    prompt = st.text_input("Ask something in Japanese or English:", placeholder="Type here...", label_visibility="visible")
    model = genai.GenerativeModel("gemini-pro")

    if st.button("SEND", use_container_width=True):
        if prompt.strip():
            try:
                # Generate response
                response = model.generate_content(prompt)

                # Display response
                st.write("<h3 style='color: blue;'>Response:</h3>", unsafe_allow_html=True)
                st.write(response.text)

            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a prompt.")

    # Additional resources tab
    with st.expander("Learn More Resources:"):
        st.markdown(
            "- [Japanese Grammar Guide](https://www.guidetojapanese.org/grammar_guide.html)\n"
            "- [JLPT Practice Tests](https://jlpt.jp/e/samples/samplequestions.html)\n"
            "- [Kanji Study](https://www.wanikani.com/)\n"
        )



if __name__ == "__main__":
    main()
