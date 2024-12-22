from flask import Flask, request, jsonify, render_template
from controllers.gemini_controller import GeminiController
from controllers.youtube_controller import YouTubeController
from controllers.openai_controller import OpenAIController
from services.gemini_service import GeminiService
from services.youtube_service import YouTubeService
from services.openai_service import OpenAIService
from dotenv import load_dotenv
import os
import requests
import openai
from PyPDF2 import PdfFileReader  # Updated import
from pytesseract import image_to_string
from PIL import Image

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize services
try:
    gemini_service = GeminiService(api_key=os.getenv('GOOGLE_API_KEY'))
    youtube_service = YouTubeService(api_key=os.getenv('YOUTUBE_API_KEY'))
    openai_service = OpenAIService(api_key=os.getenv('OPENAI_API_KEY'))

    # Initialize controllers
    gemini_controller = GeminiController(gemini_service)
    youtube_controller = YouTubeController(youtube_service)
    openai_controller = OpenAIController(openai_service)
except Exception as e:
    print(f"Error initializing services: {str(e)}")
    raise

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gemini', methods=['POST'])
def handle_gemini():
    return gemini_controller.handle_request(request)

@app.route('/youtube', methods=['POST'])
def handle_youtube():
    return youtube_controller.handle_request(request)

@app.route('/openai', methods=['POST'])
def handle_openai():
    return openai_controller.handle_request(request)

if __name__ == '__main__':
    app.run(debug=True)