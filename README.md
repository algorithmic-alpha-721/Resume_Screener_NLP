# Resume Screener

An AI-powered tool that analyzes and ranks resumes against job descriptions using Natural Language Processing (NLP).

## Features

- Resume and Job Description Parsing
- Text Preprocessing and Cleaning
- Semantic Embeddings with SentenceTransformers
- Cosine Similarity Matching
- Feedback Generation

## Tech Stack

- Python 3.9+
- Pandas
- NLTK
- SentenceTransformers
- scikit-learn

## How to Run

1. Clone the repository:
   ```bash
    git clone https://github.com/algorithmic-alpha-721/Resume_Screener_NLP.git
    cd Resume_Screener_NLP

2. Set up a virtual environment:

   python -m venv venv
   venv\Scripts\activate  # on Windows

3. Install dependencies:

   pip install -r requirements.txt


4. Place your resumes.csv and jobs.csv in the data/ folder.

5. Run the analyzer:

   python src/analyzer.py

License

This project is licensed under the MIT License.



---

### 📋 Create a requirements.txt

To list your project's dependencies, create a `requirements.txt` file with the following content:


```txt
pandas
nltk
sentence-transformers
scikit-learn
