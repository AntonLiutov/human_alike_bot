from datetime import datetime
from pyChatGPT import ChatGPT
import constants as keys

api = ChatGPT(keys.CHAT_GPT_SESSION)

def sample_responses(input_text):
    user_message = str(input_text).lower()

    response = api.send_message(user_message)
    return response["message"]

    # if user_message in ('hello', 'hi', 'sup', 'привет', 'привіт'):
    #     return "Hey! How's it going?"
    #
    # if user_message in ('who are you', 'who are you?'):
    #     return "I am a bot"
    #
    # if user_message in ('time', 'time?'):
    #     now = datetime.now()
    #     date_time = now.strftime('%d/%m/%y, %H:%M:%S')
    #
    #     return str(date_time)
    #
    # if user_message == "image":
    #     return "https://raw.githubusercontent.com/fbsamples/original-coast-clothing/main/public/styles/male-work.jpg"
    #
    # if user_message == "audio":
    #     return "http://www.largesound.com/ashborytour/sound/brobob.mp3"
    #
    # if user_message == "video":
    #     return "https://www.appsloveworld.com/wp-content/uploads/2018/10/640.mp4"
    #
    # if user_message == "file":
    #     return "http://www.africau.edu/images/default/sample.pdf"

    return "I don't understand you."
