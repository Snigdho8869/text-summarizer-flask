# Text Summarizer with BART Pretrained Model

This repository contains a Flask-based web application that utilizes the BART (Bidirectional and Auto-Regressive Transformer), GPT-2 pretrained models for text summarization. BART, GPT-2 are transformer-based models that can perform a wide range of natural language processing tasks, including summarization.

The application allows users to input a piece of text and generates a summary of that text using the BART model. The maximum length of the input text is limited to 1024 tokens, and the generated summary is limited to a maximum length of 1024 tokens.

# Requirements:

* Python 

* Flask 

* Hugging Face Transformers

* PyTorch 

# Usage:

* Clone this repository to your local machine.

* Install the required dependencies.

* Run the application using python app.py.

* Access the application by navigating to http://localhost:5000 in your web browser.

# How it Works?

The application limits the maximum length of the input text to 1024 tokens, and the generated summary is limited to a maximum length of 1024 tokens. The BART, GPT-2 models used in this application has been pretrained on a large corpus of text and fine-tuned specifically for the task of summarization. The application utilizes the Hugging Face Transformers library to interface with the BART, GPT-2 models and tokenize the input text.

# Application Interface:

<img align="right" alt="art" width="1000" src="https://i.ibb.co/Cv5FGhG/Screenshot-1.png">

