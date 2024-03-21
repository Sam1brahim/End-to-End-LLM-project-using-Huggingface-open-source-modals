# Import necessary libraries
import torch
from langchain.prompts import PromptTemplate
import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer

# Set up the device for GPU if available, otherwise use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define the directory where the Hugging Face local Large Language Model is stored
model_directory = r"D:\hugface\stablellm"

# Load the tokenizer and model from the specified directory
tokenizer = AutoTokenizer.from_pretrained(model_directory)  # Initialise the tokenizer
model = AutoModelForCausalLM.from_pretrained(model_directory)  # Initialise the model

model.to(device)  # Ensure the model runs on the chosen device (GPU/CPU)

# Define a function to generate responses based on technology and operating system
def getllmresponse(technology_name, operating_systems):
    # Define a prompt template for the query
    template = """
    Give me the best way to implement {technology_name} technology on one of these operating systems {operating_systems}. Do not forget that I am a complete beginner. So please be detailed.
    """
    # Create a prompt instance with specified variables and template
    prompt = PromptTemplate(input_variables=['technology_name', 'operating_systems'], template=template)
    # Format the prompt with actual values and encode it for the model
    input_ids = tokenizer.encode(prompt.format(technology_name=technology_name, operating_systems=operating_systems), return_tensors="pt").to(device)
    # Generate a response from the model without updating model weights
    with torch.inference_mode():
        output_ids = model.generate(input_ids, max_length=700, num_return_sequences=1)
    # Decode the generated IDs back to text
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return output_text
    
# Streamlit UI setup
# Configure the page with title and layout settings
st.set_page_config(page_title="Generate Blogs",
                   layout='centered',
                   initial_sidebar_state='collapsed')

# Display a simple page title
st.header('Technology Implementation')

# Create two columns for input fields
col1, col2 = st.columns([5, 5])

with col1:
    technology_name = st.text_input('Technology you want to implement')  # Input for technology name

with col2:
    operating_systems = st.selectbox('Operating Systems', ('Windows', 'Kali Linux', 'Ubuntu', 'MacOS Sierra'), index=0)  # Dropdown for selecting OS

# Button to trigger the generation process
submit = st.button('Generate')

# Call the response generation function when the button is clicked and display the result
if submit:
    st.write(getllmresponse(technology_name, operating_systems))
