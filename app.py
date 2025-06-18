# app.py - Flask Backend without External API Key Dependencies

from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all origins.
# In a production environment, you should restrict this to your specific frontend domain(s)
# For example: CORS(app, resources={r"/api/*": {"origins": "https://yourfrontenddomain.com"}})
CORS(app)

@app.route('/')
def home():
    """
    A simple home endpoint to confirm the API is running.
    """
    return "✅ EduGenie (Backend - No External AI API) is running. Use POST /generate-content with a JSON body."

@app.route('/generate-content', methods=['POST'])
def generate_content():
    """
    This endpoint simulates content generation without using an external AI API.
    It takes a 'title' from the request JSON and returns a basic,
    hardcoded course outline.
    """
    course_title = request.json.get('title')

    if not course_title:
        # Return a 400 Bad Request error if the title is missing
        return jsonify({"error": "Course title is required!"}), 400

    # --- SIMULATED CONTENT GENERATION ---
    # Since we are not using an external AI API (like OpenAI),
    # this part will generate a static or very simple, rule-based response.
    # Replace this logic with your desired non-AI content generation.
    simulated_outline = f"""
**Course Outline for: {course_title}**

**Course Objectives:**
* Understand the fundamental concepts of {course_title}.
* Explore practical applications and case studies related to {course_title}.
* Develop basic skills for working with {course_title}.

**Sample Syllabus:**
* **Week 1:** Introduction to {course_title} - What it is and why it matters.
* **Week 2:** Core Principles and Building Blocks.
* **Week 3:** Practical Examples and Hands-on Exercises.
* **Week 4:** Future Trends and Advanced Concepts (No AI involved!).

**Learning Outcomes:**
* Students will be able to define key terms in {course_title}.
* Students will understand the basic workflow of {course_title}.
* Students will identify common challenges in {course_title}.

**Assessment Methods:**
* Participation and Discussion
* Short Assignments
* Final Project (based on provided templates)

**Recommended Readings:**
* "The Basics of {course_title}" by [Placeholder Author 1]
* "Exploring {course_title}" by [Placeholder Author 2]
"""

    try:
        # In a real scenario, you might have complex logic here to
        # generate content based on templates, rules, or local data,
        # without calling an external AI service.
        generated_content = simulated_outline.strip()
        return jsonify({"content": generated_content})
    except Exception as e:
        # General error handling
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# To run this Flask app locally (for testing):
# 1. Save this code as app.py
# 2. Make sure you have Flask and Flask-CORS installed:
#    pip install Flask Flask-CORS
# 3. Run from your terminal: python app.py
#    (or for development with auto-reload: flask --app app run --debug)
# This will start the server, typically on http://127.0.0.1:5000/
if __name__ == '__main__':
    # Run the app in debug mode for development purposes
    app.run(debug=True)
# Note: In production, set debug=False and configure a proper WSGI server.
# Ensure you have Flask and Flask-CORS installed in your environment:
# pip install Flask Flask-CORS