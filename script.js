document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("course-form");
    const output = document.getElementById("content");
  
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
  
      const title = document.getElementById("course-title").value.trim();
  
      if (!title) {
        output.textContent = "❌ Please enter a course title!";
        return;
      }
  
      output.textContent = "⏳ Generating content, please wait...";
  
      try {
        const response = await fetch("http://127.0.0.1:5000/generate-content", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ title: title })
        });
  
        const data = await response.json();
  
        if (data.content) {
          output.textContent = data.content;
        } else if (data.error) {
          output.textContent = "❌ Error: " + data.error;
        } else {
          output.textContent = "⚠️ Unexpected response format.";
        }
      } catch (error) {
        output.textContent = "🚨 Network error: " + error.message;
      }
    });
  });
