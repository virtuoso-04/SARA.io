import requests
import openai

# === CONFIGURATION ===
OPENAI_API_KEY = "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"  # Replace with your OpenAI API key
GOOGLE_API_KEY = "AIzaSyA8WnYyEq8ZRTWfUXWIlYzsyOV6CTI31iQ"  # Replace with your Google Custom Search API key
GOOGLE_CSE_ID = "AIzaSyC5HMl5u98AuSxuFQ_BKDpCh8CSnMlxJgw"    # Replace with your Custom Search Engine ID

# Set up OpenAI API
openai.api_key = OPENAI_API_KEY

def simplify_content(raw_text):
    """
    Simplify a given text using OpenAI's GPT API.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": f"Explain this concept in simple terms: {raw_text}"}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"Error simplifying content: {e}"

def search_articles(query):
    """
    Search for articles using the Google Custom Search API.
    """
    try:
        url = f"https://www.googleapis.com/customsearch/v1"
        params = {
            "key": GOOGLE_API_KEY,
            "cx": GOOGLE_CSE_ID,
            "q": query,
        }
        response = requests.get(url, params=params)
        data = response.json()

        # Extract article titles and links
        results = []
        for item in data.get("items", []):
            title = item.get("title")
            link = item.get("link")
            results.append({"title": title, "link": link})

        return results
    except Exception as e:
        return f"Error fetching articles: {e}"

def main():
    print("Welcome to the Topic Simplifier!")
    topic = input("Enter a topic: ")

    # Step 1: Fetch raw articles using Google Custom Search
    print("Fetching related articles...")
    articles = search_articles(topic)

    # Step 2: Combine article snippets (or use Wikipedia for explanation)
    if isinstance(articles, list) and len(articles) > 0:
        raw_text = " ".join([article["title"] for article in articles])
    else:
        raw_text = "Unable to fetch related articles."

    # Step 3: Simplify the content using OpenAI's GPT
    print("Simplifying the explanation...")
    simplified_text = simplify_content(raw_text)

    # Output the results
    print("\n=== Simplified Explanation ===")
    print(simplified_text)

    print("\n=== Related Articles ===")
    if isinstance(articles, list):
        for idx, article in enumerate(articles[:5], start=1):  # Limit to top 5 articles
            print(f"{idx}. {article['title']} ({article['link']})")
    else:
        print(articles)

if __name__ == "__main__":
    main()
