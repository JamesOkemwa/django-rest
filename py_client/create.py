import requests

endpoint = 'http://127.0.0.1:8000/api/products/'

data = {
    'title': 'Sushi',
    'price': '49.99'
}
res = requests.post(endpoint, json=data)

print(res.json())


