import requests

class YouTubeService:
    def __init__(self, api_key):
        self.api_key = api_key

    def search_videos(self, query):
        try:
            url = f"https://www.googleapis.com/youtube/v3/search"
            params = {
                "key": self.api_key,
                "part": "snippet",
                "q": query,
                "type": "video",
                "maxResults": 5
            }
            response = requests.get(url, params=params)
            data = response.json()

            results = []
            for item in data.get("items", []):
                title = item["snippet"]["title"]
                description = item["snippet"]["description"]
                video_id = item["id"]["videoId"]
                link = f"https://www.youtube.com/watch?v={video_id}"
                results.append({"title": title, "description": description, "link": link})

            return results
        except Exception as e:
            return f"Error fetching YouTube videos: {e}"