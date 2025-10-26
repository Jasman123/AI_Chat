# app.py
import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Text Generation App", layout="centered")
st.title("📝 Hugging Face Text Generation with Streamlit")

# Select model (you can change this to any Hugging Face model)
model_name = st.selectbox(
    "Choose a model",
    ["gpt2", "distilgpt2", "EleutherAI/gpt-neo-125M"]
)

# Initialize the text generation pipeline
@st.cache_resource
def load_model(model_name):
    return pipeline("text-generation", model=model_name)

generator = load_model(model_name)

# User input
prompt = st.text_area("Enter your prompt:", "Once upon a time")

# Generation parameters
max_length = st.slider("Max length of generated text", 50, 500, 150)
num_return_sequences = st.slider("Number of outputs", 1, 5, 1)

if st.button("Generate"):
    with st.spinner("Generating text..."):
        outputs = generator(
            prompt,
            max_length=max_length,
            num_return_sequences=num_return_sequences,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95
        )
    st.success("✅ Generated Text:")
    for i, out in enumerate(outputs):
        st.markdown(f"**Output {i+1}:** {out['generated_text']}")
