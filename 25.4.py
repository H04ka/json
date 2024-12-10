import json

with open('products.json', 'r') as dip:
    data = json.load(dip)
for products in data['products']:
    if products['price'] > 100:
        print(products['name'])