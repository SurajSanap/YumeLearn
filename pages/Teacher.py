import openai
import streamlit as st
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Function to set API key
def set_api_key(api_key: str):
    """Set OpenAI API key for the session."""
    if api_key:
        openai.api_key = api_key
        st.session_state["api_key"] = api_key
    else:
        st.warning("Please provide a valid OpenAI API key.")

# Sidebar for API Key Input
st.sidebar.title("API Key Setup")
api_key_input = st.sidebar.text_input("Enter your OpenAI API key", type="password")

if st.sidebar.button("Set API Key"):
    set_api_key(api_key_input)

# Ensure the user has entered an API key
if "api_key" not in st.session_state or not st.session_state["api_key"]:
    st.sidebar.warning("Please enter your OpenAI API key to continue.")
    st.stop()

# Define the prompt template
prompt_template = PromptTemplate(
    input_variables=["question"],
    template=(
        "You are a Japanese language teacher. Your expertise includes grammar, vocabulary, Kanji, "
        "and conversational skills. You provide JLPT practice materials and cultural insights about Japan. "
        "Your tone is friendly, engaging, and professional. Always provide clear and structured responses "
        "tailored to the user's proficiency level.\n\n"
        "Question: {question}\n"
        "Answer:"
    )
)

# Initialize the OpenAI LLM
llm = OpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Create the LLMChain
chatbot_chain = LLMChain(llm=llm, prompt=prompt_template)

def get_response(question):
    """Generate a response using LangChain and OpenAI."""
    try:
        response = chatbot_chain.invoke({"question": question})
        return response["text"]
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit app UI
st.title("Japanese Teacher Chatbot")
st.write("Ask me anything about the Japanese language or culture!")

# User input
user_question = st.text_area("Enter your question here:")

if st.button("Submit"):
    if user_question:
        with st.spinner("Thinking..."):
            answer = get_response(user_question)
        st.write("**ChatBot:**", answer)
    else:
        st.error("Please enter a question.")
