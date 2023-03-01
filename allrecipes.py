from bs4 import BeautifulSoup
import requests
import difflib


def checkmatches(option, target):
    return difflib.SequenceMatcher(a=option.lower(), b=target.lower()).ratio()


threshold = 0.5

wordtomatch = ['crabmeat', 'distilled white vinegar', 'okra']
words = set(wordtomatch)
# without gives status code
html_text = requests.get(
    'https://www.allrecipes.com/recipe/216888/good-new-orleans-creole-gumbo/').text
soup = BeautifulSoup(html_text, 'lxml')

ingredients = soup.find_all('span', {'data-ingredient-name': True})
for ingredient in ingredients:
    print(ingredient.text)
    for word in words:
        if checkmatches(ingredient.text, word) > threshold:
            print(ingredient)
