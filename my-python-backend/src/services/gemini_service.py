import requests

class GeminiService:
    def __init__(self, api_key):
        self.api_key = api_key

    def search_articles(self, query):
        try:
            url = f"https://www.googleapis.com/customsearch/v1"
            params = {
                "key": self.api_key,
                "cx": os.getenv("GOOGLE_CSE_ID"),
                "q": query,
            }
            response = requests.get(url, params=params)
            data = response.json()

            results = []
            for item in data.get("items", []):
                title = item.get("title")
                link = item.get("link")
                snippet = item.get("snippet")
                results.append({"title": title, "link": link, "snippet": snippet})

            return results
        except Exception as e:
            return f"Error fetching articles: {e}"