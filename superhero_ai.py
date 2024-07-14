from flask import Flask, request, jsonify
import requests
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download necessary NLTK packages (comment out if already downloaded)
nltk.download('vader_lexicon')

def get_gemini_response(prompt):
  """Sends prompt to Gemini API and returns response (replace with actual implementation)"""
  # Replace with your actual Gemini API interaction code
  # This example uses a placeholder URL
  url = "AIzaSyAJqNXXbjSV6frr3EC9BnQFVOlbr2MmuXM" + prompt
  response = requests.get(url)
  return response.json()

def analyze_sentiment(text):
  """Uses NLTK to analyze sentiment of text."""
  analyzer = SentimentIntensityAnalyzer()
  return analyzer.polarity_scores(text)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  # Serve the front-end HTML
  return app.send_static_file('index.html')

@app.route('/get_response', methods=['POST'])
def get_assistant_response():
  user_query = request.json['query']

  # Sentiment Analysis (basic example)
  sentiment = analyze_sentiment(user_query)
  response_message = f"2B: "
  if sentiment['compound'] > 0.5:
    response_message += "Glad to hear you're feeling positive! "
  elif sentiment['compound'] < -0.5:
    response_message += "Sounds like you might be needing some assistance. "
  else:
    response_message += "Here to help in any way I can. "

  # Use Gemini for information retrieval or task completion
  if "find information about" in user_query:
    topic = user_query.split("find information about")[1].strip()
    response = get_gemini_response(f"find information about {topic}")
    response_message += f"\nRetrieved information from Gemini:\n {response['text']}"
  elif "what is the best way to" in user_query:
    task = user_query.split("what is the best way to")[1].strip()
    response = get_gemini_response(f"best way to {task}")
    response_message += f"\nAnalyzed with Gemini: Here might be a good approach:\n {response['text']}"
  else:
    # Handle other cases or delegate to Gemini for more complex queries
    response = get_gemini_response(user_query)
    response_message += f"\nAnalyzed with Gemini:\n {response['text']}"

  return jsonify({'response': response_message})

if __name__ == '__main__':
  app.run(debug=True)
