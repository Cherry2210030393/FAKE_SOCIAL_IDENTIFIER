import spacy

nlp = spacy.load("en_core_web_sm")

def analyze_bio(bio_text):
    doc = nlp(bio_text.lower())
    keywords = ["fan", "backup", "parody", "not real", "not official", "impersonation"]
    return any(keyword in doc.text for keyword in keywords)