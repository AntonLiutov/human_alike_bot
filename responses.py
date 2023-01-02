from datetime import datetime
from pyChatGPT import ChatGPT
import constants as keys

api = ChatGPT(keys.CHAT_GPT_SESSION)

def sample_responses(input_text):
    user_message = str(input_text).lower()

    response = api.send_message(user_message)
    return response["message"]
