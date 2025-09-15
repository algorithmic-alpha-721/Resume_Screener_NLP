import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

def clean_text(text: str) -> str:
    """Basic text cleaning"""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)  # remove special chars
    tokens = [word for word in text.split() if word not in stop_words]
    return " ".join(tokens)
