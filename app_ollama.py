# Importing the necessary modules from the Streamlit and LangChain packages
import streamlit as st
from langchain_community.llms import Ollama

llm = Ollama(
    model="phi3"
)  # assuming you have Ollama installed and have llama3 model pulled with `ollama pull llama3 `

# Setting the title of the Streamlit application
st.title('Ollama Simple LLM-App ')

# Defining a function to generate a response using the OpenAI language model
def generate_response(input_text):
    # Initializing the OpenAI language model with a specified temperature and API key
    llm = Ollama(model="phi3",temperature=0.7)
    # Displaying the generated response as an informational message in the Streamlit app
    st.info(llm(input_text))

# Creating a form in the Streamlit app for user input
with st.form('my_form'):
    # Adding a text area for user input
    text = st.text_area('Enter text:', '')
    # Adding a submit button for the form
    submitted = st.form_submit_button('Submit')
    # If the form is submitted and the API key is valid, generate a response
    if submitted :
        generate_response(text)