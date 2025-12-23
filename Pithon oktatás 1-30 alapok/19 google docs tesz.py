import requests

url = "https://docs.google.com/document/d/1GEoB8DBz2HzOU46l-CPBlAFspuwQOaLOwor9PtnAEpc/export?format=txt"
res = requests.get(url)
print(res.text)