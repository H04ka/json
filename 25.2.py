import json

name_book = {'name': 'Novgorotsev v grante',
        'autor': 'Minyailo',
        'year publication': 2024}

with open('book.json', 'w') as json_data:
    book = json.dump(name_book, json_data)
    print(book)