print("Задание", 1)
import json

with open ('data.json', 'r') as json.data:
    data = json.load(json.data)
    print(data['name'], data['city'])



