EduGenie: AI-Powered Educational Content Creator

Project Overview

EduGenie is a web-based tool that leverages OpenAI's API to dynamically generate educational content based on a user-provided course title. The tool generates a course objective, sample syllabus, three measurable learning outcomes aligned with Bloom's Taxonomy, assessment methods, and recommended readings. It features a simple UI, robust error handling, and ensures data privacy by not storing user inputs.

Features





User Input: Users enter a course title via a web form.



AI-Generated Content: Generates structured educational content using OpenAI's API.



Bloom's Taxonomy Alignment: Learning outcomes are designed to align with various levels of Bloom's Taxonomy (e.g., remembering, understanding, applying, analyzing, evaluating, creating).



Error Handling: Handles invalid inputs, API errors, and parsing issues gracefully.



Data Privacy: No user data is stored; inputs are processed ephemerally.



Responsive UI: Built with Tailwind CSS for a clean, user-friendly interface.

Tech Stack





Backend: Python, Flask, OpenAI API



Frontend: HTML, JavaScript, Tailwind CSS



Environment: Python 3.8+, Flask, python-dotenv, openai-python

Setup Instructions





Clone the Repository:

git clone <repository-url>
cd edugenie



Install Dependencies:

pip install flask flask-cors openai python-dotenv



Set Up Environment Variables:





Create a .env file in the project root.



Add your OpenAI API key:

OPENAI_API_KEY=your-api-key-here



Run the Flask Server:

python app.py



Access the Application:





Open a browser and navigate to http://localhost:5000.



Place the index.html file in the templates folder or serve it statically.

Usage





Enter a course title (e.g., "Introduction to Python Programming") in the input field.



Click "Generate Content" to fetch AI-generated educational content.



View the structured output, including course objective, syllabus, learning outcomes, assessment methods, and recommended readings.

Testing





Unit Tests: Test API endpoints using tools like pytest to ensure correct responses.



UI Tests: Verify input validation and content display using browser developer tools.



Edge Cases: Test with empty inputs, invalid course titles, and API failures.



Bloom's Taxonomy Verification: Manually review generated learning outcomes to confirm alignment with Bloom's levels.

Data Privacy





No user inputs are stored on the server.



API requests are made securely using HTTPS.



Ensure your OpenAI API key is kept confidential and not exposed in the frontend.

Limitations





Requires an active internet connection for OpenAI API calls.



Dependent on the quality and consistency of OpenAI's responses.



Limited to text-based content generation.

Future Improvements





Add support for selecting specific Bloom's Taxonomy levels.



Implement user authentication for personalized content generation.



Enhance the UI with additional styling and interactivity.

Troubleshooting





API Errors: Ensure your OpenAI API key is valid and you have sufficient quota.



CORS Issues: Verify that Flask-CORS is properly configured.



Content Parsing: If the AI response isn't valid JSON, the fallback response will display "N/A".

License

MIT License