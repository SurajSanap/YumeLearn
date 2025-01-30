import streamlit as st
import pandas as pd
import os

# Available JLPT levels (including "Select" as default)
JLPT_LEVELS = ["Select", "N5", "N4", "N3", "N2", "N1"]

# Streamlit Page
st.title("📖 JLPT Vocabulary")

# Sidebar Dropdown for Level Selection
selected_level = st.sidebar.selectbox("Select JLPT Level", JLPT_LEVELS, index=0)

# Display message when "Select" is chosen
if selected_level == "Select":
    st.info("Please select a JLPT level to view vocabulary.")
else:
    # Correct file path using os.path.join
    file_path = os.path.join("data", "Vocab", f"{selected_level}_Vocab.txt")

    # Load and Display Vocabulary
    if os.path.exists(file_path):
        try:
            # Read vocabulary file
            data = []
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split("|")
                    if len(parts) == 3:
                        data.append(parts)

            # Convert to DataFrame
            df = pd.DataFrame(data, columns=["Col1", "Col2", "Col3"])

            # Display Table
            st.write(f"### {selected_level} Vocabulary List")
            st.dataframe(df, use_container_width=True)

        except Exception as e:
            st.error(f"Error loading vocabulary: {e}")
    else:
        st.warning(f"Vocabulary file for {selected_level} not found.")

# Footer
st.markdown(
    """
    <footer style="text-align: center; margin-top: 50px;">
        © 2025 YumeLearn
    </footer>
    """,
    unsafe_allow_html=True,
)
