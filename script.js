document.getElementById('course-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const courseTitle = document.getElementById('course-title').value;
    
    if (!courseTitle) return;
  
    try {
      const response = await fetch('http://localhost:5000/generate-content', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: courseTitle }),
      });
  
      const data = await response.json();
      
      document.getElementById('content').textContent = JSON.stringify(data, null, 2);
      document.getElementById('content-output').style.display = 'block';
    } catch (error) {
      console.error('Error:', error);
    }
  });
  
  // Inside your script.js
const API_BASE_URL = "http://127.0.0.1:5000"; // Or the actual IP/port your Flask app is running on

// ... (rest of your existing script.js code)

generateBtn.addEventListener('click', async () => {
    const courseTitle = courseTitleInput.value.trim();
    // ... (loading, error handling)

    if (!courseTitle) {
        // ... (error message)
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/generate-content`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ title: courseTitle })
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Failed to generate content');
        }

        const data = await response.json();
        generatedContentDiv.innerHTML = `<pre>${data.content}</pre>`;

    } catch (error) {
        errorMessageDiv.innerText = `Error: ${error.message}`;
        errorMessageDiv.style.display = 'block';
        console.error('API call error:', error);
    } finally {
        loadingIndicator.style.display = 'none';
    }
});