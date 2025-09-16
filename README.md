# 📄 Resume Screener

An **AI-powered tool** that analyzes and ranks resumes against job descriptions using **Natural Language Processing (NLP)**.  
This project helps recruiters automatically filter, compare, and rank candidates by leveraging semantic embeddings.

---

## 🚀 Features
- 📑 Resume & Job Description Parsing  
- 🧹 Text Preprocessing and Cleaning (stopwords, lemmatization, etc.)  
- 🔍 Semantic Embeddings with **SentenceTransformers**  
- 📈 Cosine Similarity Matching for ranking resumes  
- 💬 Feedback Generation for candidate-job fit  

---

## 🧰 Tech Stack
- **Python 3.9+**
- **Pandas** → Data handling  
- **NLTK** → Preprocessing  
- **SentenceTransformers** → Semantic embeddings  
- **scikit-learn** → Similarity & evaluation  

---

## ⚡ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/algorithmic-alpha-721/Resume_Screener_NLP.git
cd Resume_Screener_NLP
```
### 2. Set up a virtual environment
```bash
# Create venv
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Prepare datasets
```bash
data/resumes.csv
data/jobs.csv
```

### 5. Run the analyzer
```bash
python src/analyzer.py
```

## Requirements
To list your project’s dependencies, include a requirements.txt file with:
- pandas
- nltk
- sentence-transformers
- scikit-learn

---
## Author
**Developed by Aj (algorithmic-alpha-721)**
**Inspired by real-world hiring challenges and NLP innovation.**

---

Do you also want me to add **shields.io badges** (Python version, MIT license, NLP, etc.) at the very top to make it pop on GitHub like a pro repo?
