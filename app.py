# Load the required packages
import streamlit as st
from groq import Groq

# Intialize the streamlit app
st.set_page_config(page_title="GEN AI Project Llama 3.3")

# Load the API key
api_key = st.secrets["GROQ_API_KEY"]

# Intialize the Groq API
client = Groq(api_key = api_key)

# Function to generate the model response
def get_reponse(text,model_name="llama-3.3-70b-versatile"):
    stream = client.chat.completions.create(
        messages = [
            {
                "role":"system",
                "content":"You are a helpful assistant"
            },
            {
                "role":"user",
                "content":text
            }
        ],
        model = model_name,
        stream = True
    )

    for chunk in stream:
        response  = chunk.choices[0].delta.content
        if response is not None:
            yield response
    
# Add the title to streamlit app
st.title("Gen AI project using Llama 3.3 model")
st.subheader("by Sindhura Nadendla")

# Provide text area for user input
user_ip =  st.text_area("Ask your question: ")

# Create submit button
submit = st.button("Generate",type="primary")

# Write the code that retrieves response when user clicks on submit
if submit:
    st.subheader("Model Response: ")
    st.write_stream(get_reponse(user_ip))