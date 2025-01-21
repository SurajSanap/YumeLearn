import os
import streamlit as st
from PIL import Image

# Paths for additional PDF resources
PDF_FOLDER = "data\PDF"

# Default thumbnail image (make sure this image is in your project folder)
DEFAULT_THUMBNAIL = "assets/Book.png"  # Ensure this file exists in your project folder

import json
from streamlit_lottie import st_lottie


# Animation Section
try:
    with open('assets\Library.json', encoding='utf-8') as anim_source:
        animation_data = json.load(anim_source)
        st_lottie(animation_data, height=200, key="About")
except FileNotFoundError:
    st.error("Animation file not found. Please check the file path.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")

# PDF data for Books section
books = [
    {"name": "Tanki Master Drill N5", "url": "https://drive.google.com/uc?id=1rLzj4PQCbGv-yo1jJKS8ZHFJN2WpYYDO"},
    {"name": "Nihongo Challenge Kanji N4-N5", "url": "https://drive.google.com/uc?id=1wXRVM9drU2RqcdB65SVWxZmM-lmHQEhp"},
    {"name": "JLPT N5 Grammar", "url": "https://drive.google.com/uc?id=1D6dU0qt1DVO5bNdhoe34ra6B8mRE52Dz"},
    {"name": "Japanese Reading Practice", "url": "https://drive.google.com/uc?id=1R1v1DIEE5U1ry_PIMd52Uc-rhVa9SVxS"},
    {"name": "JLPT Vocabulary", "url": "https://drive.google.com/uc?id=1R_JB5QjQgnmLrgBoob06-L-FIarhwsPV"},
    {"name": "N5 Listening Practice", "url": "https://drive.google.com/uc?id=1ARUNt-E67sKpg3f9TJFAAY-V7X1JQRAx"},
]

# PDF data for Papers section
papers = [
    {"name": "JLPT N1 Official Practice Workbook", "url": "https://www.jlpt.jp/e/samples/sample12.html"},
    {"name": "JLPT N2 Official Practice Workbook", "url": "https://www.jlpt.jp/e/samples/sample12.html"},
    {"name": "JLPT N3 Official Practice Workbook", "url": "https://www.jlpt.jp/e/samples/sample12.html"},
    {"name": "JLPT N4 Official Practice Workbook", "url": "https://www.jlpt.jp/e/samples/sample12.html"},
    {"name": "JLPT N5 Official Practice Workbook", "url": "https://www.jlpt.jp/e/samples/sample12.html"},
]

# Helper function to list PDFs by level
def list_pdfs_by_level(level):
    """Lists all PDF files in the folder for the given JLPT level."""
    level_folder = os.path.join(PDF_FOLDER, level)
    if os.path.exists(level_folder):
        return [f for f in os.listdir(level_folder) if f.endswith(".pdf")]
    return []

# Streamlit App
st.title("PDF Bookshelf")

# Load the default thumbnail once
try:
    default_image = Image.open(DEFAULT_THUMBNAIL)
except FileNotFoundError:
    st.error(f"Default image '{DEFAULT_THUMBNAIL}' not found. Please add it to your project folder.")
    default_image = None

# Books Section
st.header("Books")
if default_image:
    book_cols = st.columns(4)  # Adjust the number of columns as needed
    for idx, book in enumerate(books):
        with book_cols[idx % len(book_cols)]:
            st.image(default_image, use_container_width=True)
            st.markdown(f"[**{book['name']}**]({book['url']})", unsafe_allow_html=True)

# Papers Section
st.header("Papers")
if default_image:
    paper_cols = st.columns(4)  # Adjust the number of columns as needed
    for idx, paper in enumerate(papers):
        with paper_cols[idx % len(paper_cols)]:
            st.image(default_image, use_container_width=True)
            st.markdown(f"[**{paper['name']}**]({paper['url']})", unsafe_allow_html=True)

# JLPT PDFs Section
st.header("JLPT PDF Resources by Level")
levels = ["N5", "N4", "N3", "N2", "N1"]
selected_level = st.sidebar.radio("Select JLPT Level:", levels)

# Display PDFs for the selected level
st.subheader(f"JLPT {selected_level} PDFs")
pdf_files = list_pdfs_by_level(selected_level)
if pdf_files:
    for pdf in pdf_files:
        file_path = os.path.join(PDF_FOLDER, selected_level, pdf)
        st.write(f"📄 {pdf}")
        with open(file_path, "rb") as file:
            st.download_button(label=f"Download {pdf}", data=file, file_name=pdf)
else:
    st.write(f"No PDFs available for JLPT {selected_level}.")

# Footer
st.markdown(
    """
    <footer style="text-align: center; margin-top: 50px;">
        © 2025 YumeLearn
    </footer>
    """,
    unsafe_allow_html=True,
)
