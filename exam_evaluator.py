# -*- coding: utf-8 -*-
"""Exam_Evaluator.ipynb
"""

!pip install gradio
!pip install PyPDF2
import gradio as gr
from transformers import pipeline
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import PyPDF2

def extract_text_from_pdf(pdf_path):
    # Extract text from the PDF file
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
    return text

def calculate_cosine_similarity(text1, text2):
    vectorizer = CountVectorizer().fit_transform([text1, text2])
    vectors = vectorizer.toarray()
    return cosine_similarity(vectors)[0][1]

def evaluate(question, pdf_file, student_answer, total_marks):
    # Convert total_marks to an integer
    total_marks = int(total_marks)

    # Extract text from the provided PDF
    pdf_text = extract_text_from_pdf(pdf_file)

    # Use the model to predict the answer
    model = pipeline('question-answering', model='distilbert-base-cased-distilled-squad')
    predicted_answer = model(question=question, context=pdf_text)['answer']

    # Calculate the cosine similarity between the student's answer and the predicted answer
    similarity = calculate_cosine_similarity(student_answer, predicted_answer)

    # Split the student's answer and the predicted answer into individual words
    student_words = student_answer.lower().split()
    predicted_words = predicted_answer.lower().split()

    # Calculate the cosine similarity for each word in the student's answer with each word in the predicted answer
    word_similarities = {}
    for student_word in student_words:
        for predicted_word in predicted_words:
            word_similarity = calculate_cosine_similarity(student_word, predicted_word)
            word_similarities[(student_word, predicted_word)] = word_similarity

    # Compare the overall similarity with a threshold (e.g., 0.3)
    if similarity > 0.3:
        result = "Correct"
        score = total_marks  # Assign full marks when the answer is correct
    else:
        result = "Incorrect"
        score = 0

    # Provide an explanation
    explanation = f"The predicted answer was '{predicted_answer}'. The overall cosine similarity is {similarity:.2f}. Based on the cosine similarity, the answer is {result}. The score for this answer is {score} out of {total_marks}."

    return explanation, word_similarities

iface = gr.Interface(
    fn=evaluate,
    inputs=["text", "file", "text", "number"],
    outputs=["text", "text"]
)
iface.launch()
