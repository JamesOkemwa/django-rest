import requests

# endpoint = 'https://httpbin.org/status/200'
endpoint = 'https://httpbin.org/anything'
endpoint = 'http://127.0.0.1:8000/api/'

res = requests.get(endpoint, params={"abc": 123}, json={"query": "Hello World"})

# print(res.text)
# print(res.status_code)
print(res.json())


