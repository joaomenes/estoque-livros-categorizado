import json

def categorie(locates: str) -> str:

    data_books = "dados/books_named.json"

    with open(data_books, "r") as file:
        reading: list[dict, any] = json.load(file)            # é uma lista

    categories: list[str] = [book['category'] for book in reading]

    if locates in categories:
        return print(f'Há {categories.count(locates)} books nessa categoria.')
    else: 
        return print('Indisponível')

try:
    locates = str(input('Qual categoria deseja procurar? ')).upper()

    if len(locates) != 1:
        raise ValueError  # Levanta um erro se a entrada não for uma letra

except ValueError:
    print('Digite apenas uma letra.')

categorie(locates)