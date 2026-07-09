import streamlit as st
import sys
from pathlib import Path
# Adding the project root to Python's path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from backend.app import generate_incident_response

st.html("""
<style>
div[data-testid="stTextInput"] {
    width: 500px !important;
}
</style>
""")
image_dir = Path(__file__).resolve().parent.parent / "images"
st.set_page_config(
    page_title="DST AI Assistant",
    page_icon=image_dir / "logo.jpg"
)

with st.container(horizontal=True):
    st.image(image_dir / "logo.jpg", width=50)
    st.header("DST AI Assistant", divider=True, anchor=False)

user_input_heading = st.text_area("Provide logs or ask questions for the agent: ")

# Submit button
if st.button("Submit"):
    with st.spinner("Processing response, please wait..."):
        (output, times) = generate_incident_response(user_input_heading)
    st.write(times)
    st.write(output)
  
    