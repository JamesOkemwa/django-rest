import requests

# endpoint = 'https://httpbin.org/status/200'
endpoint = 'https://httpbin.org/anything'

res = requests.get(endpoint, json={"query": "Hello World"})

print(res.json())


