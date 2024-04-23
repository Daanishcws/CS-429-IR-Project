# CS-429-IR-Project

## Abstract
This project involves the development of an information retrieval system constructed using Python. The system includes a web crawler built with Scrapy, an indexer using scikit-learn for creating an inverted index with TF-IDF scoring, and a query processor implemented in Flask to handle real-time queries and return the top-k ranked results. The objective is to provide a fully functional retrieval system that can process and respond to user queries efficiently. Future enhancements may include implementing advanced features like semantic search and automated query correction.

## Overview
The proposed system is designed to crawl, index, and process queries on HTML documents retrieved from specified URLs. The project integrates technologies like Scrapy for web crawling, scikit-learn for indexing documents, and Flask for processing queries. This system is primarily aimed at educational purposes to demonstrate the capabilities of a basic search engine.

## Design
### System Capabilities
- Crawling web pages up to a specified depth and number of pages.
- Indexing the content of these pages using a vector space model with TF-IDF weighting.
- Processing incoming queries through a Flask-based web interface, validating them, and returning the top-k results based on cosine similarity.
### Interactions
- Users input queries through a web form.
- The system processes these queries and displays ranked results.
### Integration
- Integrates Python libraries such as NLTK and scikit-learn for text processing and vector space modeling.
## Architecture
**Crawler**: Utilizes Scrapy to fetch HTML documents based on a given seed URL, maximum pages, and depth.
**Indexer**: Built with scikit-learn, it creates an inverted index that stores documents and their TF-IDF scores.
**Processor**: A Flask application that accepts queries in JSON format, processes them against the indexed data, and returns ranked results.
## Operation
### Software Commands
- 'flask run': Starts the server.
- Environment variables set up for development or production modes.
- Running Components:
  1. Crawler: ``` scrapy crawl PokeCrawler.py ```
  2. Indexer: ``` python build_index.py ```
  3. Processor: ``` python mainpro.py ```
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
- Wikipedia contributors. "Pokémon." Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/Pok%C3%A9mon
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
