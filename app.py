import os
import google.generativeai as genai
from flask import Flask, jsonify, request
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='error.log', level=logging.DEBUG)

# Configure the Google API key
os.environ['GOOGLE_API_KEY'] = 'YOUR_GOOGLE_API_KEY_HERE'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Initialize the generative model and chat
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

@app.route('/')
def hello_world():
    app.logger.debug('Hello world endpoint was called')
    return "Gracy's Gemini!"

@app.route('/gemini', methods=['POST'])
def gemini_response_chat():
    data = request.json
    app.logger.debug(f'Received data: {data}')
    try:
        query = data.get('query')
        response = chat.send_message(query)
        app.logger.debug(f'Response from chat: {response.text}')
        return jsonify({'response': response.text})
    except Exception as e:
        app.logger.error(f'Error processing request: {e}')
        return jsonify({'error': str(e)}), 500

# Remove or comment out the app.run() line for PythonAnywhere deployment
# if __name__ == "__main__":
#     app.run()
