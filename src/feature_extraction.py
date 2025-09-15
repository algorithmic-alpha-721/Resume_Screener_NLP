from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer

# TF-IDF extractor
def get_tfidf_features(resumes, jobs):
    vectorizer = TfidfVectorizer(max_features=5000)
    all_texts = resumes + jobs
    X = vectorizer.fit_transform(all_texts)
    return X, vectorizer

# SBERT embeddings
sbert = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(texts):
    return sbert.encode(texts, convert_to_tensor=True)
