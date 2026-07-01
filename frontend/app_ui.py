import streamlit as st
import sys
from pathlib import Path

st.html("""
<style>
div[data-testid="stTextInput"] {
    width: 500px !important;
}
</style>
""")

# Add the project root to Python's path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from backend.app import logs_output

image_dir = Path(__file__).resolve().parent.parent / "images"

with st.container(horizontal=True):
    st.image(image_dir / "logo.jpg", width=50)
    st.header("DST AI Assistant", divider=True, anchor=False)

logs = st.text_area("Logs:")

# Submit button
if st.button("Submit"):
    with st.spinner("Processing response, please wait..."):
        output = logs_output(logs)
    st.write(output)
    