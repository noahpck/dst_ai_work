import streamlit as st
import sys
from pathlib import Path

# Add the project root to Pythons path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import main

logs = st.text_area("Logs")

if st.button("Submit"):
    output = main(logs)
    st.write(output)