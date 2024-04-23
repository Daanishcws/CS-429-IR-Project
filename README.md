# CS-429-IR-Project

## Abstract
This project aims to develop a web-based search engine using Flask and Python to demonstrate the application of information retrieval techniques with an inverted index. The objective was to build an efficient and scalable system for searching text documents. Future work may involve enhancing the user interface, improving the ranking algorithms, and expanding the document corpus.

## Overview
The solution implements a Flask web application that allows users to search for text documents. The system employs natural language processing and machine learning techniques to process and rank documents based on relevance to the search query. Key literature and systems studied include the book "Introduction to Information Retrieval" by Manning et al., which served as a foundation for the implemented algorithms.

## Design
### System Capabilities
- Text search with relevance ranking
- Interactive web interface
- Real-time query processing
### Interactions
- Users input queries through a web form.
- The system processes these queries and displays ranked results.
### Integration
- Integrates Python libraries such as NLTK and scikit-learn for text processing and vector space modeling.
## Architecture
### Software Components
- 'Flask' for the web server.
- 'nltk' for text processing.
- 'scikit-learn' for implementing TF-IDF vectorization.
### Interfaces
- Web-based user interface accessible via browser.
- RESTful API endpoints for search functionality.
### Implementation
- Python scripts handle backend logic.
- HTML and CSS for front-end presentation.
## Operation
### Software Commands
- 'flask run': Starts the server.
- Environment variables set up for development or production modes.
### Inputs
- User enters text queries through the web interface.
### Installation
- Dependencies are listed in requirements.txt and installed via 'pip'.
- Setup instructions are provided in the README.
## Conclusion
The system successfully implements a basic search engine with document ranking. While effective in demonstrating core IR principles, it may require optimizations for handling larger datasets or more complex queries. Future enhancements could include implementing additional NLP features or adopting more sophisticated ranking algorithms.

## Data Sources
- Sample text documents used in this project were sourced from open-source datasets.
## Test Cases
### Framework
- Python's 'unittest' framework for backend testing.
- Integration tests simulate user interactions with the web interface.
### Harness
- Automated tests validate the search functionality and ranking accuracy.
### Coverage
- Tests cover major functionalities including query processing, document retrieval, and error handling.
### Source Code
- The source code is fully documented and available in the GitHub repository.
- Dependencies are clearly listed and open-source, ensuring transparency and ease of installation.
### Bibliography
- Manning, C. D., Raghavan, P., & Schütze, H. (2008). Introduction to Information Retrieval. Cambridge University Press.
- "Flask Documentation" (2024). Flask. https://flask.palletsprojects.com/
- "Scikit-learn: Machine Learning in Python," Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.
- OpenAI. "ChatGPT: Optimizing Language Models for Dialogue." OpenAI Blog. https://www.openai.com/chatgpt

## Brief Instructions

### Software Commands
To set up and run the search engine, follow these commands in your terminal:

#### 1. Install Dependencies:
Ensure you have Python installed, then run:
``` pip install -r requirements.txt ```

This command installs all necessary libraries including Flask, ntlk, numpy, and scikit-learn as specified in your 'requirements.txt' file.

#### 2. Start the server:
Launch the Flask server by running:
``` flask run ```
or
``` python -m flask run ```
This command starts the web application on localhost on the default port 5000.

### Interacting with the Web Interface
#### 1. Access the Web Interface:
Open a web browser and go to http://127.0.0.1:5000/ to access the main page.
#### 2. Submitting Queries:
- Use the search box to type your query, it should be in this form
  ``` http://127.0.0.1:5000/search?query=example ```
- Hit the "submit" button to process your search.
- The search results will be displayed on the page, showing document IDs and their scores based on relevance.
### Tips for Use
- Ensure that your server is running before trying to access the web interface.
- If changes are made to the code, the server may need to be restarted to reflect these changes.
