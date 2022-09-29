import requests

endpoint = 'http://127.0.0.1:8000/api/products/10/update/'

data = {
    'title': 'New Sushi',
    'price': '129.99'
}
res = requests.put(endpoint, json=data)

print(res.json())


