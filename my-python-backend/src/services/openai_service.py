import openai

class OpenAIService:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def simplify_content(self, raw_text):
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

    def calculate_relevance(self, topic, text):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "user", "content": f"How relevant is this text to the topic '{topic}'? Rate it on a scale of 0 to 10: {text}"}
                ]
            )
            return response.choices[0].message['content']
        except Exception as e:
            return f"Error calculating relevance: {e}"