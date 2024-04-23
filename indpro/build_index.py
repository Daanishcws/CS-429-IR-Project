import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ensure necessary NLTK resources are downloaded
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def load_data(json_file):
    logging.info(f"Loading data from {json_file}")
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
        logging.info("Data loaded successfully")
        return data
    except FileNotFoundError:
        logging.error(f"File {json_file} not found")
        return []
    except json.JSONDecodeError:
        logging.error("Error decoding JSON")
        return []

def preprocess_data(data):
    logging.info("Starting data preprocessing")
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    corpus = []
    for item in data:
        text = item['content'].lower()
        tokens = word_tokenize(text)
        filtered_tokens = [stemmer.stem(word) for word in tokens if word not in stop_words and word.isalnum()]
        corpus.append(' '.join(filtered_tokens))
    logging.info("Data preprocessing completed")
    return corpus

def build_index(corpus):
    logging.info("Building the index")
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names_out()
    index = {word: [] for word in feature_names}
    for idx, word in enumerate(feature_names):
        doc_list = tfidf_matrix[:, idx].tocoo()  # Convert column to COO format
        for doc_idx, value in zip(doc_list.row, doc_list.data):
            index[word].append((doc_idx, value))
    logging.info("Index built successfully")
    return index, vectorizer

def save_object(obj, filename):
    logging.info(f"Saving object to {filename}")
    with open(filename, 'wb') as out_file:
        pickle.dump(obj, out_file)
    logging.info(f"Object saved to {filename}")

def main():
    json_file = 'output.json'  # Path to your JSON file
    data = load_data(json_file)
    if data:
        corpus = preprocess_data(data)
        index, vectorizer = build_index(corpus)
        save_object(index, 'inverted_index.pkl')
        save_object(vectorizer, 'vectorizer.pkl')

if __name__ == '__main__':
    main()
