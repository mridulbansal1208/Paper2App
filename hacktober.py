import streamlit as st
from PIL import Image
from google import genai
from google.genai import types

st.set_page_config(page_title="Gemma Multimodal Inspector", layout="centered")

st.title("📁 Upload File for Gemma Analysis")
st.write("Upload an image (sketch, screenshot, note) to get a full technical analysis and code.")

# 1. Initialize client
@st.cache_resource
def get_client():
    return genai.Client()

client = get_client()

# 2. Browser file uploader
uploaded_file = st.file_uploader("Choose an image file...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image")

    # Action button
    if st.button("Run Gemma Analysis", type="primary"):
        with st.spinner("Analyzing image with Gemma..."):
            prompt = """
            You are a senior UI/UX engineer and systems architect.
            Analyze the provided hand-drawn design, wireframe, or whiteboard:

            1. Overview: 1-2 sentence executive summary of the interface.
            2. Component Inventory: Bullet points of all detected elements and controls.
            3. Frontend Prototype: 
               i. Ignore explanatory notes and labels: Never render handwritten notes (e.g., 'controls opacity', 'points to north', 'adjustable clock') as text on screen. Convert them into functional, styled UI controls instead.
               ii. Professional Design System:
                 - Use glassmorphism (e.g., backdrop-blur-md, bg-white/10, border border-white/20).
                 - Use clean SVG icons or Heroicon paths instead of emojis.
                 - For sliders, use actual styled HTML5 inputs or styled track/thumb components.
                  - For constellations, draw neat SVG lines with glowing circular nodes.
               iii. Deliverable: Provide a standalone HTML file wrapped in a mobile phone frame (390px x 844px) inside a ```html ... ``` code block. Include Tailwind via CDN.
            4. Audit: Highlight missing edge cases, ambiguous labels, and touch/ergonomics bottlenecks (thumb zone, accessibility).
            """

            try:
                response = client.models.generate_content(
                    model="gemma-4-26b-a4b-it",
                    contents=[img, prompt],
                    config=types.GenerateContentConfig(temperature=0.2),
                )
                
                # Directly output the raw text results
                st.markdown("---")
                st.subheader("Analysis Results")
                st.markdown(response.text)

            except Exception as err:
                st.error(f"Error during analysis: {err}")