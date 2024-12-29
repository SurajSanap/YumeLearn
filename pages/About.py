import json
import streamlit as st
from streamlit_lottie import st_lottie

# Add page title

st.set_page_config(page_title="YumeLearn", page_icon="assets/jp9.gif", layout="wide", initial_sidebar_state="expanded")

# Animation Section
try:
    with open('assets/About.json', encoding='utf-8') as anim_source:
        animation_data = json.load(anim_source)
        st_lottie(animation_data, height=200, key="About")
except FileNotFoundError:
    st.error("Animation file not found. Please check the file path.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")

# About Me Section
st.title("About Me")

st.write("""
Hi! I'm 
        <p style="font-size: 24px; font-weight: bold;">
        <span style="color: orange;">Suaj Sanap,</span>
        </p>
        a passionate developer with expertise in **AI**, **Machine Learning**, and building web applications. 
I love solving real-world problems using innovative technologies.
""", 
    unsafe_allow_html=True)

# Define URLs for GitHub and LinkedIn
github_url = "https://github.com/SurajSanap"
linkedin_url = "https://www.linkedin.com/in/SurajSanap01"

st.markdown("### Connect with me:")

# Create two columns
col1, col2 = st.columns(2)

# GitHub button on the left
with col1:
    st.markdown(
        f"""
        <a href="{github_url}" target="_blank">
            <button style="padding: 10px; font-size: 16px; color: white; background-color: #333; border: none; border-radius: 5px; width: 100%;">
                GitHub
            </button>
        </a>
        """,
        unsafe_allow_html=True,
    )

# LinkedIn button on the right
with col2:
    st.markdown(
        f"""
        <a href="{linkedin_url}" target="_blank">
            <button style="padding: 10px; font-size: 16px; color: white; background-color: #0072b1; border: none; border-radius: 5px; width: 100%;">
                LinkedIn
            </button>
        </a>
        """,
        unsafe_allow_html=True,
    )

# My Projects Section
st.header("My Projects")

st.divider()

# Define project data
projects = [
    {
        "id": 1,
        "title": "College.ai",
        "description": "AI-based platform to optimize job applications using Generative AI. Features include ATS, Resume Analyzer, and PDF Chat powered by NLP and LLMs.",
        "image": "https://github.com/SurajSanap/College.ai-main/assets/101057653/f5923134-c4c1-4586-975b-3247675bb475",
        "tags": ["Streamlit", "Langchain", "Google Gemini API", "SQLite", "NLP", "LLMs"],
        "github": "https://github.com/SurajSanap/College.ai-main",
        "webapp": "https://collegeai.streamlit.app/"
    },
    {
        "id": 2,
        "title": "CultiVision",
        "description": "Developed a website offering real-time crop recommendations with regression and data modeling based on soil and pest analysis.",
        "image": "https://github.com/user-attachments/assets/328fff0d-4ad5-4dd3-b8c5-c1a44fe2fae4",
        "tags": ["HTML", "CSS", "ML", "DL", "Active Learning", "Bayesian Models"],
        "github": "https://github.com/SurajSanap/Cultivision",
        "webapp": "https://placeholder.app"
    },
    {
        "id": 3,
        "title": "My Future Stock",
        "description": "Designed and deployed a machine learning model to forecast global stock prices, addressing the challenge of accurate stock market predictions using regression and data modeling techniques.",
        "image": "https://akm-img-a-in.tosshub.com/businesstoday/images/story/202306/gettyimages-1311007681-2afbfba73b744b88ab3bd388ae6c8b00_2-sixteen_nine.jpg?size=948:533",
        "tags": ["Python", "Flask", "Regression", "Machine Learning", "SQL"],
        "github": "https://github.com/SurajSanap/My-Future-Stock",
        "webapp": "https://placeholder.app"
    }
]


# Display projects in a cleaner format
for project in projects:
    st.subheader(project["title"])
    st.image(project["image"], use_container_width=True)
    st.markdown(f"**Description:** {project['description']}")
    st.markdown(f"**Tags:** {', '.join(project['tags'])}")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"[GitHub Repo]({project['github']})")
    with col2:
        st.markdown(f"[Live Demo]({project['webapp']})")
    st.divider()



#Side Bar




# Buttons for GitHub and LinkedIn
with st.sidebar:
    st.image("assets/SRS.png")


    if st.button("GitHub"):
        st.write(f"Redirecting to [GitHub Profile]({github_url})...")
        st.query_params(url=github_url)

    if st.button("LinkedIn"):
        st.write(f"Redirecting to [LinkedIn Profile]({linkedin_url})...")
        st.query_params(url=linkedin_url)


  
st.markdown("""
    

## Books
* [GENKI](http://genki.japantimes.co.jp/index_en)
* [TOBIRA](http://tobiraweb.9640.jp/)

## Reading

* [NHK Easy News](http://www3.nhk.or.jp/news/easy/) 
* [Japanese Folktales](http://www.e-hon.jp/ehon_jp/index1.htm) 
* [Hukumusume Fairy Tale Collection](http://hukumusume.com/douwa/) 
* [用例.jp](http://yourei.jp/) 
* [Satori Reader](https://www.satorireader.com/) 
* [Keio University Reading Materials Bank](http://language.tiu.ac.jp/materials/jpn/index.html) 
* [Mlle Claire Froelich's guide](http://www.guidetojapanese.org/learn/)

## Podcast
* [Learn Japanese Pod](https://learnjapanesepod.com/) 
* [JapanesePod101](https://www.japanesepod101.com/) 
* [News in Slow Japanese](http://newsinslowjapanese.com/) 
* [NHK News Podcast](http://www.nhk.or.jp/podcasts/) 
* [Bilingual News](http://bilingualnews.libsyn.com/) 

## Community

* [/r/learnjapanese](https://www.reddit.com/r/LearnJapanese/) 
* [Discord](https://discordapp.com/) 
	* [English-Japanese Language Exchange](https://discord.gg/NJJCYVD) 
	* [日本語と英語](https://discord.gg/0eIsYvFQul270V1L) 
	* [Reddit Masterlist](https://www.reddit.com/r/languagelearning/comments/5m5426/discord_language_learning_servers_masterlist/) 
* [HelloTalk](https://www.hellotalk.com/) - Popular language exchange app.

            
            
""")


