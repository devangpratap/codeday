const submitBtn = document.getElementById('submit-btn');
const userQueryInput = document.getElementById('user-query');
const responseDiv = document.getElementById('response');

submitBtn.addEventListener('click', async () => {
  const userQuery = userQueryInput.value.trim();
  if (userQuery) {
    try {
      // Send the user query to the Python backend using fetch
      const response = await fetch('/get_response', {
        method: 'POST',
        body: JSON.stringify({ query: userQuery }),
        headers: { 'Content-Type': 'application/json' }
      });
  
      if (!response.ok) {
        throw new Error(`Error fetching response: ${response.statusText}`);
      }
  
      const data = await response.json();
      responseDiv.textContent = data.response;
      userQueryInput.value = '';
    } catch (error) {
      console.error('Error fetching response:', error);
      responseDiv.textContent = 'An error occurred. Please try again later.';
    }
  }
});
