from flask import request, jsonify
from services.youtube_service import YouTubeService

class YouTubeController:
    def __init__(self, youtube_service):
        self.youtube_service = youtube_service

    def handle_request(self, request):
        query = request.json.get('query', '')
        videos = self.youtube_service.search_videos(query)
        return jsonify({'videos': videos})