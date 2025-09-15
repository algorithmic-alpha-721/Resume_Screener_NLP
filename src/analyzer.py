from src.preprocess import clean_text
from src.feature_extraction import get_embeddings
from sentence_transformers.util import cos_sim

def analyze_resume_jd(resume_text, jd_text):
    """Compare resume with job description using embeddings"""
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)

    embeddings = get_embeddings([resume_clean, jd_clean])
    sim_score = cos_sim(embeddings[0], embeddings[1]).item()

    return {
        "similarity_score": round(sim_score * 100, 2),
        "feedback": "Good match" if sim_score > 0.7 else "Needs improvement"
    }



    

if __name__ == "__main__":
    resume = "Experienced in Python, Machine Learning, SQL, Tableau"
    jd = "Looking for Data Scientist with Python, SQL, Machine Learning, AWS"
    result = analyze_resume_jd(resume, jd)
    print(result)
