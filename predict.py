import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Get email content
email = input("Enter Email Content: ")

# Convert text to vector
email_vector = vectorizer.transform([email])

# Predict
prediction = model.predict(email_vector)

print("Prediction:", prediction[0])

# Change the condition based on your dataset labels
if prediction[0] == 1:
    print("⚠️ Phishing Email Detected")
else:
    print("✅ Safe Email")