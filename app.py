import re
import fitz  # PyMuPDF
from flask import Flask, render_template, request, flash
import traceback

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Clean text (remove links, punctuation, and extra whitespace)
def clean_text(text):
    try:
        text = re.sub(r'http\S+\s*', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s]', '', text)
        return text.strip().lower()
    except Exception as e:
        print("Error in clean_text:", e)
        return text

# Extract contact number using regex
def extract_contact_number(text):
    try:
        # Match international and local formats
        pattern = r"(?:\+?\d{1,4}[\s-]?)?(?:\(?\d{2,5}\)?[\s-]?)?\d{3,5}[\s-]?\d{3,5}"
        matches = re.findall(pattern, text)

        # Return the first valid-looking number with 10+ digits
        for match in matches:
            digits_only = re.sub(r'\D', '', match)
            if 10 <= len(digits_only) <= 15:
                return match.strip()
    except Exception as e:
        print("Error in extract_contact_number:", e)
    return None


# Skill matcher (case insensitive)
def extract_skills(text):
    try:
        skills_list = [
            "Python", "Java", "JavaScript", "C", "C++", "React.js", "Node.js",
            "SQL", "AWS", "Docker", "TensorFlow", "Pandas", "NLP", "Power BI"
        ]
        found = []
        for skill in skills_list:
            if skill.lower() in text:
                found.append(skill)
        return found
    except Exception as e:
        print("Error in extract_skills:", e)
        return []

# Resume text extractor using fitz (for PDF or .txt)
def extract_text_from_file(uploaded_file):
    filename = uploaded_file.filename.lower()
    try:
        if filename.endswith(".pdf"):
            doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            text = ""
            for page in doc:
                text += page.get_text()
            return text
        elif filename.endswith(".txt"):
            return uploaded_file.read().decode("utf-8", errors="ignore")
        else:
            return ""
    except Exception as e:
        print("Error in extract_text_from_file:", e)
        return ""

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method == "POST":
            uploaded_file = request.files.get("resume")
            if not uploaded_file or uploaded_file.filename == "":
                flash("Please upload a resume file.", "danger")
                return render_template("index.html")

            resume_text = extract_text_from_file(uploaded_file)
            if not resume_text:
                flash("Unsupported file or unreadable content.", "warning")
                return render_template("index.html")

            cleaned_text = clean_text(resume_text)
            contact = extract_contact_number(cleaned_text)
            skills = extract_skills(cleaned_text)

            # Placeholder category logic
            predicted_category = "Software Engineer" if "python" in cleaned_text else "Unknown"

            return render_template("index.html",
                                   contact=contact,
                                   skills=skills,
                                   category=predicted_category)

        return render_template("index.html")
    except Exception as e:
        print("Unhandled Exception:", e)
        traceback.print_exc()
        flash("An unexpected error occurred. Please try again.", "danger")
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
