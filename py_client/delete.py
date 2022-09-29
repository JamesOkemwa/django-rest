import requests

product_id = input('What is the product id you want to use? \n')

try:
    product_id = int(product_id)
except:
    print(f"{product_id} is not a valid id")
    product_id = None

if product_id:
    endpoint = f'http://127.0.0.1:8000/api/products/{product_id}/delete/'

    res = requests.delete(endpoint)

    print(res.status_code, res.status_code == 204)


