from flask import Flask, request, jsonify
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

app = Flask(__name__)

# Load the serialized objects
def load_object(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None

# Attempt to load resources
index = load_object('inverted_index.pkl')
vectorizer = load_object('vectorizer.pkl')

# Check if the necessary resources are loaded
if not index or not vectorizer:
    print("Failed to load one or more necessary files. Please ensure 'inverted_index.pkl' and 'vectorizer.pkl' are available.")

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip()
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    print(f"Query received: {query}")

    # Process the query using the vectorizer
    try:
        query_vec = vectorizer.transform([query]).toarray()[0]
    except Exception as e:
        return jsonify({'error': 'Failed to process the query', 'message': str(e)}), 500

    scores = {}
    for word, postings in index.items():
        if word in vectorizer.vocabulary_:
            word_idx = vectorizer.vocabulary_[word]
            query_score = query_vec[word_idx]
            if query_score > 0:
                for doc_id, doc_score in postings:
                    if doc_id not in scores:
                        scores[doc_id] = 0
                    scores[doc_id] += doc_score * query_score

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    results = [{'document_id': int(doc_id), 'score': float(score)} for doc_id, score in sorted_scores]

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
