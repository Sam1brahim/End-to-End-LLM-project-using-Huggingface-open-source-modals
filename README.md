# End-to-End-LLM-project-using-Huggingface-open-source-modals

Technology Implementation Assistant

This project harnesses the power of a pretrained Large Language Model (LLM) from Hugging Face, combined with the interactivity of Streamlit, to provide detailed, beginner-friendly guides on implementing various technologies across different operating systems. It's designed for absolute beginners looking for step-by-step instructions tailored to their technology and operating system choice. Also a great view for developer to learn how to harness the powers of LLM locally.
Features: 

    * Pretrained Language Model: Utilizes a local copy of a Hugging Face model for generating responses.
    * Custom Prompts: Dynamically generates prompts based on user input to provide specific, detailed guides.
    * Streamlit Interface: Offers an easy-to-use web interface for inputting your technology and operating system preferences and viewing the generated implementation guide.
    * GPU/CPU Support: Automatically detects and utilizes GPU for faster processing, with a fallback to CPU if necessary.

Getting Started
Prerequisites

    Python 3.8+
    PyTorch
    Transformers
    Streamlit
    An available GPU is recommended but not required.
    A downloaded LLM from Huggingface ( it can be sharded or one bin file )

Installation:
Clone the repository to your local machine:

   bash
   git clone https://github.com/yourusername/technology-implementation-assistant.git

Navigate to the project directory.
Install the required dependencies:

   pip install -r requirements.txt

Running the Application:

* Ensure you have the Hugging Face model downloaded to a local directory, e.g., D:\hugface\stablellm.

* Start the Streamlit application:

   bash
   streamlit run app.py

Open your web browser and navigate to the URL provided by Streamlit, usually http://localhost:8501.

Use the interface to enter the technology you're interested in and select an operating system. Click "Generate" to receive your guide.


# Remark : 
* It can take a huge computational power ( more than langchain community ollama ). So be advised. 

Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.
