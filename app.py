import os
import google.generativeai as genai
from flask import Flask, render_template, jsonify, request, redirect, url_for, session



os.environ['GOOGLE_API_KEY'] = 'AIzaSyDpp_vnAlO1-1_2TcPsDGm4dhN41F2ZPCU'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
app = Flask(__name__)

model = genai.GenerativeModel('gemini-pro')
chat = model .start_chat(history=[])

@app.route('/')
def hello_world():
    return "Gracy's Live"

@app.route(rule='/gemini',methods=['POST'])
def gemini_response_chat()->str:
    query=request.json
    response = chat.send_message(query)
    return response.text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500,debug=True)
