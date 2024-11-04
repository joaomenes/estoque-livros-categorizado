import json

data_books = "dados/books_named.json"

with open(data_books, "r") as file:
    lendo = json.load(file)
    #print(lendo)

dicionario_books = {books ['title'] : books ['category'] for books in lendo}

print(dicionario_books.values())