import spacy
from spacy.matcher import PhraseMatcher

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample list of common skills (you can expand this list as needed)
common_skills = [
    "python", "java", "aws", "docker", "machine learning", "data science",
    "project management", "cloud computing", "databases", "tensorflow",
    "deep learning", "flask", "django", "git", "linux", "devops"
]


# Function to parse resume text with improved skill extraction
def parse_resume(text):
    doc = nlp(text)
    name, email, phone = None, None, None
    skills = []

    # PhraseMatcher for skills extraction
    matcher = PhraseMatcher(nlp.vocab)
    patterns = [nlp(skill) for skill in common_skills]
    matcher.add("SKILLS", None, *patterns)

    # Extract entities and match against skills
    for ent in doc.ents:
        if ent.label_ == "PERSON" and not name:
            name = ent.text
        elif re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', ent.text):
            email = ent.text
        elif re.match(r'\+?\d[\d -]{8,}\d', ent.text):
            phone = ent.text

    # Use matcher to extract skills from the text
    matches = matcher(doc)
    for match_id, start, end in matches:
        span = doc[start:end]
        skills.append(span.text.lower())

    # Clean up and deduplicate skills
    skills = list(set(skills))

    # Fallback for email extraction if not found via NER
    if not email:
        email_matches = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
        if email_matches:
            email = email_matches[0]

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills,  # Return unique skills extracted
    }
