from flask import jsonify

class GeminiController:
    def __init__(self, gemini_service):
        self.gemini_service = gemini_service

    def handle_request(self, request):
        query = request.json.get('query', '')
        articles = self.gemini_service.search_articles(query)
        return jsonify({'articles': articles})