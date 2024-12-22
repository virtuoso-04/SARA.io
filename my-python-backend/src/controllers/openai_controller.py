class OpenAIController:
    def __init__(self, openai_service):
        self.openai_service = openai_service

    async def generate_summary(self, req, res):
        user_input = req.json.get('input')
        summary = await self.openai_service.get_summary(user_input)
        res.json({'summary': summary})

    async def fetch_response(self, req, res):
        user_input = req.json.get('input')
        response = await self.openai_service.get_response(user_input)
        res.json({'response': response})

    def handle_request(self, request):
        raw_text = request.json.get('text', '')
        simplified_text = self.openai_service.simplify_content(raw_text)
        return jsonify({'simplified_text': simplified_text})