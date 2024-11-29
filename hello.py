import streamlit as st
from PIL import Image
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# Configure API key
genai.configure(api_key="AIzaSyAUyBs_riC8BmDBjR4HV8P0D_wx5pI_e2U")

def generate_test(text_prompt, image_input=None):
    model = genai.GenerativeModel("gemini-1.5-flash")
    # Check if both text and image are provided
    if text_prompt and image_input:
        response = model.generate_content([text_prompt, image_input])
    elif text_prompt:
        response = model.generate_content([text_prompt])
    elif image_input:
        response = model.generate_content([image_input])
    else:
        response = None
    return response.text if response else "No input provided."

# Streamlit UI
st.set_page_config(page_title="CHAT GPT 4")
st.header("GPT 4")
text_prompt = st.text_input("Input prompt:", key="input")


uploaded_image = st.file_uploader("Choose an image:", type=["jpg", "png", "jpeg"])
image_input = None
if uploaded_image is not None:
    image_input = Image.open(uploaded_image)
    st.image(image_input, caption="Uploaded Image", use_column_width=True)


submit = st.button("Generate Response")
if submit:
    response = generate_test(text_prompt, image_input)
    st.subheader("The response is:")
    st.write(response)
