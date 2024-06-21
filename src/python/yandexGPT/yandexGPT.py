import requests

prompt = {
    "modelUri": "gpt://b1g41s6646vhf6c6i6ic/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 0.6,
        "maxTokens": "2000"
    },
    "messages": [
        {
            "role": "system",
            "text": "Ты проффесиональный Java программист из Yandex."
        },
        {
            "role": "user",
            "text": "Что такое Spring Framework?"
        }
        # {
        #     "role": "assistant",
        #     "text": "Привет! Чтобы овладеть Силой, тебе нужно понять ее природу. Сила находится вокруг нас и соединяет всю галактику. Начнем с основ медитации."
        # },
        # {
        #     "role": "user",
        #     "text": "Хорошо, а как насчет строения светового меча? Это важная часть тренировки джедая. Как мне создать его?"
        # }
    ]
}


url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key AQVNz6ubmslpQbo-ylMwQEuX7dXuQzWYh3G6IS06"
}

response = requests.post(url, headers=headers, json=prompt)
result = response.text
print(result)