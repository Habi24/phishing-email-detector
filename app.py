import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Page title
st.title("📧 Phishing Email Detection")

st.write("Enter an email message below to check whether it is Phishing or Safe.")

# Text area
email = st.text_area("Email Content")

# Predict button
if st.button("Check Email"):

    if email.strip() == "":
        st.warning("Please enter an email message.")
    else:
        email_vector = vectorizer.transform([email])
        prediction = model.predict(email_vector)

        if prediction[0] == 1:
            st.error("⚠️ Phishing Email Detected")
        else:
            st.success("✅ Safe Email")