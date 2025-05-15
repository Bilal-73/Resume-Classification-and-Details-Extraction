🧠 Resume Category Classification — Project Explanation
📌 Objective:
To develop a web-based machine learning application that:

Accepts resumes in .pdf or .txt format.

Extracts text and features.

Predicts the job category of the resume using a trained Random Forest classifier with TF-IDF.

Optionally extracts named entities (skills, contact info) for better interpretability.

📂 Dataset Overview
We used a labeled resume dataset commonly available on Kaggle (e.g., "Resume Dataset with Multi-Class Labels").

✅ Format:
Each sample consists of:

Category: The job domain label (e.g., Data Science, HR, Software Engineer, Advocate, etc.)

Resume: The text content of the resume

📊 Sample Categories:
Category	Example Keywords
Data Science	Python, ML, Deep Learning
HR	Recruitment, Payroll, Onboarding
Web Developer	HTML, CSS, JavaScript
Software Engineer	Java, C++, Algorithms
Advocate	Legal, Law, Court

📈 Dataset Stats:
Total Samples: ~960 resumes

Total Categories: 25+

Languages: English

🔍 Data Preprocessing
We followed a clear pipeline:

Cleaning Text:

Lowercasing

Removing punctuation, digits, and stopwords

Tokenization

Feature Engineering:

TfidfVectorizer(max_features=3000)

Converts text into numeric feature vectors for classification

Model Training:

RandomForestClassifier(n_estimators=100, random_state=42)

Trained on 80% data, tested on 20%

Model Evaluation:

Accuracy: ~92% on validation set

Saved models: resume_category_model.pkl and tfidf_vectorizer.pkl

🔧 Web App Functionality
Upload:
Users can upload resumes in .txt or .pdf format.

Text is extracted using:

PyMuPDF (fitz) for PDFs

open() for text files

Prediction:
Text is preprocessed and vectorized using the saved TF-IDF model.

Category is predicted using the Random Forest model.

Extraction (Optional Enhancements):
Using spaCy NER, we extract:

Skills

Emails

Phone numbers

⚙️ Core Components
File	Description
app.py	Main Flask backend
templates/index.html	Frontend to upload and view results
train_model.py	Trains and saves the classifier and vectorizer
utils.py	Contains helper functions: text cleaning, prediction, extraction
resume_category_model.pkl	Trained model
tfidf_vectorizer.pkl	TF-IDF vectorizer

----------------------------------------------
📈 Sample Output:

📄 Uploaded Resume: John_Data_Scientist.pdf

🧠 Predicted Category: Data Science

🛠 Skills Extracted:
- Python
- Machine Learning
- Pandas
- SQL

📧 Contact Email: john.doe@email.com
📞 Phone: +1-234-567-8900

----------------------------------------------
🚀 Deployment Suggestions
You can deploy the project using:

Frontend (static): Netlify or GitHub Pages

Backend (Flask): Render, Railway, or Heroku

🌟 Improvements To Consider
Add resume scoring (based on job match)

Use BERT instead of TF-IDF + Random Forest

Add admin dashboard to manage predictions

Connect a job description input for real-time job-resume match
