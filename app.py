try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:
    # In deployment, environment variables may be provided directly.
    # Skip .env loading if python-dotenv is unavailable or shadowed.
    pass
import streamlit as st 
import os 
import google.generativeai as genai 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash") 

def my_output(query):
    response = model.generate_content(query) 
    return response.text 

#### UI Development using streamlit 

st.set_page_config(page_title="Askie")
st.header("Askie") 
input = st.text_input("Input " , key = "input")  
submit = st.button("Get Your Answer") 

if submit :
    response = my_output(input) 
    st.subheader("Output")
    st.write(response)