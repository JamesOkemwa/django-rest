import requests

endpoint = 'http://127.0.0.1:8000/api/products/'

data = {
    'title': 'Pie',
    'price': '4.99'
}
res = requests.post(endpoint, json=data)

print(res.json())


