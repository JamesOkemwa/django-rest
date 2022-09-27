import requests

# endpoint = 'https://httpbin.org/status/200'
endpoint = 'https://httpbin.org/anything'
endpoint = 'http://127.0.0.1:8000/api/'

res = requests.post(endpoint, params={"abc": 123}, json={"title": "Hello World"})

# print(res.text)
# print(res.status_code)
print(res.json())


