import streamlit as st
import sys
from pathlib import Path

st.html(
    """
    <style>
        div[data-testid="stTextInput"] {
            width: 500px !important; 
        }
    </style>
    """
)
# Add the project root to Pythons path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from app import main
image_dir = Path(__file__).resolve().parent.parent / "images"
st.image(image_dir / "logo.jpg", width=100)
logs = st.text_area("Logs:")

if st.button("Submit"):
    output = main(logs)
    st.write(output)