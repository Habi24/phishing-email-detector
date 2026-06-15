# Phishing Email Detection System

## Overview

This project is a Machine Learning-based Phishing Email Detection System developed using Python and Scikit-learn. The system analyzes email content and classifies emails as either **Phishing** or **Safe**.

## Features

* Detects phishing and legitimate emails
* Uses Natural Language Processing (NLP) techniques
* TF-IDF feature extraction
* Machine Learning classification using Naive Bayes
* Displays prediction results instantly
* Simple Streamlit web interface

  ## Dataset Information

The dataset is not included in this repository because it exceeds GitHub's file size limit.

To train the model:

1. Download a phishing email dataset from Kaggle or another source.
2. Save it in the project root directory as:

phishing_email.csv

3. Run:

python train_model.py

Note: The dataset must contain the following columns:

* text_combined
* label

Where:

* 0 = Safe Email
* 1 = Phishing Email


## Technologies Used

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Naive Bayes Classifier
* Streamlit

## Project Structure

phishing-email-detector/

├── app.py

├── predict.py

├── train_model.py

└── .gitignore

## How to Run

### Train the Model

```bash
python train_model.py
```

### Run the Streamlit Application

```bash
streamlit run app.py
```

## Sample Inputs

### Phishing Email

Click here to verify your bank account immediately.

### Safe Email

Meeting scheduled tomorrow at 10 AM.

## Expected Output

* ⚠️ Phishing Email Detected
* ✅ Safe Email

## Future Enhancements

* URL feature analysis
* Advanced Machine Learning models
* Email attachment scanning
* Real-time email monitoring

## Author

Habibunissa M
