import pytest
from unittest.mock import patch, MagicMock
from app.chatbot import Chatbot
from requests.exceptions import RequestException

API_URL = "http://fakeapi.com/chat"
HEADERS = {"Authorization": "Bearer test-token", "Content-Type": "application/json"}
SYSTEM_PROMPT = "Always respond nicely. ###"
BOT_NAME = "Bot"
USER_NAME = "User"


@pytest.fixture
def chat_instance():
    return Chatbot(
        user_name=USER_NAME,
        bot_name=BOT_NAME,
        system_prompt=SYSTEM_PROMPT,
        chat_history=[],
        api_url=API_URL,
        headers=HEADERS,
    )


def test_get_response_success(chat_instance):
    user_input = "Hello!"
    fake_bot_reply = "Hi there!"

    # Patch requests.post to return a mocked response
    with patch("app.chatbot.requests.post") as mock_post:
        mock_response = MagicMock()
        mock_response.json.return_value = {"message": fake_bot_reply}
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        reply = chat_instance.get_response(user_input)

    assert reply == fake_bot_reply
    assert chat_instance.chat_history[-2]["message"] == user_input
    assert chat_instance.chat_history[-1]["message"] == fake_bot_reply



def test_get_response_api_error(chat_instance):
    user_input = "Hello!"

    with patch(
        "app.chatbot.requests.post", side_effect=RequestException("Network error")
    ):
        reply = chat_instance.get_response(user_input)

    assert "Error:" in reply
    assert chat_instance.chat_history[-2]["message"] == user_input
    assert chat_instance.chat_history[-1]["message"] == reply
