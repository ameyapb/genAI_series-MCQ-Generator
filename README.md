# MCQs Creator App with Langchain

This is a Streamlit web application for creating multiple-choice questions (MCQs) using Langchain.
<img width="726" alt="image" src="https://github.com/ameyapb/genAI_series-MCQ-Generator/assets/67974891/dbfc89fd-4fa1-42e5-84ca-c3cc2b3e41e4">

## Description

This application allows users to:

- Upload a PDF or text file to extract content for generating MCQs [or use documents from WIKI].
- Specify the number of MCQs to generate.
- Input the subject and complexity level of the questions.
- Create MCQs based on the provided inputs.
- View the generated MCQs in a table format and review the generated questions.

## Installation

1. Clone the repository:

    ```
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Installation:

    To install this package, use setup.py:

    ```
    python setup.py install
    ```

3. Set up your OpenAI API key by creating a `.env` file in the project directory and adding your API key:

    ```
    OPENAI_API_KEY=your_openai_api_key_here
    ```

4. Run the Streamlit app:

    ```
    streamlit run app.py
    ```

## Usage

1. Upon running the Streamlit app, you will be presented with a form to input your preferences for generating MCQs.
2. Upload a PDF or text file if available. If not, leave the file upload field empty.
3. Specify the number of MCQs you want to generate, the subject, and the complexity level of the questions.
4. Click the "Create MCQ's" button to generate the MCQs.
5. Once the MCQs are generated, you will be presented with a table displaying the questions and their options.
6. You can review the generated questions in the text area below the table.

## Usage of Wikipedia API

This application utilizes the Wikipedia API to retrieve content for generating MCQs when no file is uploaded by the user. The Wikipedia API provides access to a vast repository of knowledge, allowing the application to fetch relevant information based on the user's specified subject.
