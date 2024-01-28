import streamlit as st
import spacy
from spacy.matcher import PhraseMatcher

#keywords = ["Python", "Java", "JavaScript", "Git"]

def highlight_keywords(nlp, resume, keywords):
    matcher = PhraseMatcher(nlp.vocab)
    patterns = [nlp(keyword.lower()) for keyword in keywords]
    matcher.add("Keywords", None, *patterns)
    
    doc = nlp(resume)
    matches = matcher(doc)
    
    # a set of matched spans for efficient comparison
    matched_spans = {doc[start:end].text.lower() for match_id, start, end in matches}
    
    # a list of tokens with highlighted spans
    tokens = []
    for token in doc:
        if any(keyword.lower() in token.text.lower() for keyword in keywords):
            tokens.append(f'<mark style="background-color: yellow;">{token.text}</mark>')
        else:
            tokens.append(token.text)
    
    highlighted_text = " ".join(tokens)
    return st.markdown(highlighted_text, unsafe_allow_html=True)

def show_resume_highlight_page():
    st.title("Resume Keyword Highlighter")
    st.sidebar.title("Candidate Resume")

    resume_input = st.sidebar.text_area("Paste the candidate's resume here:")

    keywords = st.sidebar.text_input("Enter keywords (comma-separated):")
    keywords = [keyword.strip() for keyword in keywords.split(",")]

    if st.sidebar.button("Highlight Keywords"):
        nlp = spacy.load("en_core_web_sm")
        highlight_keywords(nlp, resume_input, keywords)

