# Exam Evaluator

The Exam Evaluator is a simple yet powerful tool designed to assist in the grading process. It uses the BERT model from Hugging Face and cosine similarity to evaluate student answers.

## Overview

The Exam Evaluator takes a PDF document uploaded by the user, a question related to the PDF, and a student's answer to the question. It reads the PDF and converts it into textual data, which is then used as context to evaluate the correctness of the student's answer. The evaluation is done using cosine similarity, a measure of similarity between two non-zero vectors, and the BERT model from Hugging Face, a state-of-the-art machine learning model for natural language processing tasks.

## Dependencies

The project requires the following Python libraries:
- gradio
- PyPDF2
- transformers
- sklearn

You can install these dependencies using pip:

~~~bash
pip install gradio PyPDF2 transformers sklearn

~~~

## Usage
To use the Exam Evaluator, simply run the Python script. This will launch a Gradio interface where you can upload your PDF document, input your question, and input the student’s answer. The Exam Evaluator will then evaluate the student’s answer and provide a score.

## Note
This project can easily be made live on Gradio.

I hope this README file meets your requirements. If you need any further assistance, feel free to ask.
