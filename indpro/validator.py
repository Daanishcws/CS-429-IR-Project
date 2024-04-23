import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def load_object(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        print(f"Failed to load {filename}: {e}")
        return None

def inspect_index(index):
    if index is not None:
        # Print the first 10 entries of the index to get a sense of its structure
        for term, postings in list(index.items())[:10]:
            print(f"Term: {term} -> Postings: {postings[:5]}")  # Print first 5 postings for brevity

def inspect_vectorizer(vectorizer):
    if vectorizer is not None:
        # Print feature names and check vectorizer type
        print("Vectorizer type:", type(vectorizer))
        feature_names = vectorizer.get_feature_names_out()
        print("First 10 feature names:", feature_names[:10])

def main():
    # Load the inverted index and vectorizer
    index = load_object('inverted_index.pkl')
    vectorizer = load_object('vectorizer.pkl')

    # Inspect the loaded objects
    print("Inspecting Inverted Index:")
    inspect_index(index)
    print("\nInspecting Vectorizer:")
    inspect_vectorizer(vectorizer)

if __name__ == '__main__':
    main()
