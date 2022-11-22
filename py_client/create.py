import requests

endpoint = 'http://127.0.0.1:8000/api/products/'
headers = {
    "Authorization": "Bearer 837dc5c8334697edc03b54a2a805379b48babc8b"
}

data = {
    'title': 'Pie',
    'price': '4.99'
}
res = requests.post(endpoint, json=data, headers=headers)

print(res.json())


