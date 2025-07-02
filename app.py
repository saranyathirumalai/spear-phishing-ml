import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer

# Load the trained model and vectorizer
with open('naive_bayes_spam_classifier.pkl', 'rb') as file:
    NB_classifier = pickle.load(file)

with open('count_vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Function to classify email text
def classify_text(text):
    text_vectorized = vectorizer.transform([text])
    prediction = NB_classifier.predict(text_vectorized)
    if prediction[0] == 1:
        return "⚠️ This is a SPEAR PHISHING email!"
    else:
        return "✅ This is a LEGITIMATE email."

# Streamlit App
def main():
    st.set_page_config(page_title="Spear Phishing Email Detector", layout="centered")
    st.title("📧 Spear Phishing Email Detector")
    st.markdown("Use this tool to check if an email is a **legitimate** or **spear phishing** attempt using machine learning.")

    user_input = st.text_area("Enter the content of the email here:")

    if st.button("Classify"):
        if user_input.strip():
            result = classify_text(user_input)
            if "SPEAR PHISHING" in result:
                st.error(result)
            else:
                st.success(result)
        else:
            st.warning("Please enter some text to classify.")

    st.markdown("---")
    st.caption("Developed by T. Saranya | MSc Final Year Project")

if __name__ == "__main__":
    main()
