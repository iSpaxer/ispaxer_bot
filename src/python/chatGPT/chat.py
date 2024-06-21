import httpx
from typing import List, Dict

messages: List[Dict] = [{'role': 'system', 'content': "Ты эксперт в создании сайтов."}]

url = 'https://api.proxyapi.ru/openai/v1/chat/completions'
token = 'sk-NsKTbuiU05uI2vUJ6FEXxRRSMoSrbK3p'

headers = {'Content-Type': 'application/json'}


def get_response(messages: List[Dict]):
    data = {'model': 'gpt-3.5-turbo', 'messages:': messages}

    auth = ('Bearer', token)

    with httpx.Client(auth=auth, headers=headers, timeout=300) as client:
        response = client.post(url=url, json=data)
        response.raise_for_status()
    return response.json()['choices'][0]['message']['content']


def save_dialogs(role: str, content: str):
    dialog = {'role': role, 'content': content}
    messages.append(dialog)


def get_chat_gpt():
    message_user = input('Я: ')
    save_dialogs(role='user', content=message_user)
    response = get_response(messages=messages)
    print(f"ChatGPT: {response}")
    save_dialogs(role='assistant', content=response)


if __name__ == '__main__':
    get_chat_gpt()
