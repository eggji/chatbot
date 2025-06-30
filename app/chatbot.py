import requests


class Chatbot:
    def __init__(
        self,
        user_name: str,
        bot_name: str,
        system_prompt: str,
        chat_history: list,
        api_url: str,
        headers: dict,
    ):
        self.name = user_name
        self.system_prompt = system_prompt
        self.bot_name = bot_name
        self.user_name = user_name
        self.chat_history = chat_history
        self.api_url = api_url
        self.headers = headers

    def get_response(self, user_input: str) -> str:
        self.chat_history.append({"sender": self.user_name, "message": user_input})

        payload = {
            "memory": "",
            "prompt": self.system_prompt,
            "bot_name": self.bot_name,
            "user_name": self.user_name,
            "chat_history": self.chat_history,
        }

        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            data = response.json()
            bot_message = data.get("message", "No response from bot.")
        except requests.RequestException as e:
            bot_message = f"Error: {str(e)}"

        self.chat_history.append({"sender": self.bot_name, "message": bot_message})
        return bot_message
