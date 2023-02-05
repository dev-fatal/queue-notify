import requests


def get_chat_id(token):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    data = requests.get(url).json()
    try:
        chat_id = data["result"][0]["message"]["chat"]["id"]
    except IndexError:
        return None
    return str(chat_id)


def send_message(token, chat_id):
    message = "Your Solo Shuffle is ready."
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)
