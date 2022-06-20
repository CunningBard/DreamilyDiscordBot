import requests

res = requests.get("https://dreamily.ai/api")
print(res.text)