import streamlit as st
import random
import json
import os
from streamlit_lottie import st_lottie

# Load the questions from JSON files
def load_questions(level):
    file_path = f"data/Test/{level}.json"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        st.error(f"Questions for {level} not found.")
        return []

# Render the test page
def render_test_page():
    try:
        with open('assets/Exam.json', encoding='utf-8') as anim_source:
            animation_data = json.load(anim_source)
        st_lottie(animation_data, 1, True, True, "high", 350, -200)
    except FileNotFoundError:
        st.error("Animation file not found.")
    except UnicodeDecodeError as e:
        st.error(f"Error decoding JSON: {e}. Try specifying a different encoding.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
    st.title("JLPT Practice Test")

    # Select Test level
    levels = ["n5", "n4", "n3", "n2"]
    selected_level = st.selectbox("Select JLPT Level", levels, key="level_selector")

    # Load questions
    questions = load_questions(selected_level)

    if not questions:
        return

    # Display animation
    

    # Shuffle questions if not already shuffled
    if "shuffled_questions" not in st.session_state or st.session_state.current_level != selected_level:
        random.shuffle(questions)
        st.session_state.shuffled_questions = questions
        st.session_state.current_level = selected_level
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.session_state.answers = []
        st.session_state.show_next = False

    # Get the current question
    question_index = st.session_state.question_index

    if question_index < len(st.session_state.shuffled_questions):
        question = st.session_state.shuffled_questions[question_index]
        st.write(f"**Q{question_index + 1}: {question['question']}**")

        options = question["options"]
        selected_option = st.radio("Select your answer:", options, key=f"q{question_index}")

        if not st.session_state.show_next:
            if st.button("Submit Answer", key=f"submit_{question_index}"):
                st.session_state.answers.append({
                    "question": question["question"],
                    "selected": selected_option,
                    "correct": question["answer"]
                })
                if selected_option == question["answer"]:
                    st.session_state.score += 1
                st.session_state.show_next = True

        st.write(f"Remaining Questions: {len(st.session_state.shuffled_questions) - question_index - 1}")

        if st.session_state.show_next:
            if st.button("Next Question", key=f"next_{question_index}"):
                st.session_state.show_next = False
                if st.session_state.question_index + 1 < len(st.session_state.shuffled_questions):
                    st.session_state.question_index += 1
                else:
                    st.success(f"Test completed! Your score: {st.session_state.score}/{len(st.session_state.shuffled_questions)}")

                    # Show a summary of answers
                    for idx, answer in enumerate(st.session_state.answers):
                        st.write(f"Q{idx + 1}: {answer['question']}")
                        st.write(f"Your answer: {answer['selected']} | Correct answer: {answer['correct']}")

                    if st.button("Restart Test"):
                        del st.session_state.shuffled_questions
                        st.session_state.current_level = None
                        st.session_state.question_index = 0
                        st.session_state.answers = []
                        st.session_state.score = 0

    # Sidebar
    with st.sidebar:
        try:
            sidebar_animation_path = os.path.join("assets", "SakuraAnimation.json")
            with open(sidebar_animation_path, encoding='utf-8') as anim_source:
                sidebar_animation = json.load(anim_source)
            st_lottie(sidebar_animation, height=150, key="sidebar_animation")
        except FileNotFoundError:
            st.error("Sidebar animation file not found.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

    # Footer
    st.markdown(
        """
        <footer style="position: fixed; bottom: 0; width: 100%; background-color: #2c2f33; color: white; text-align: center; padding: 10px;">
            © 2025 Suraj Sanap Project
        </footer>
        """,
        unsafe_allow_html=True,
    )

# Main
if __name__ == "__main__":
    render_test_page()
