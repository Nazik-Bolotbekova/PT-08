import requests

from bs4 import BeautifulSoup

class Game:
    def __init__(self, name, image, price):
        self.name = name
        self.image = image
        self.price = price

    @classmethod
    def from_soup(cls, name, image, price):
        return cls(name, image, price)

    def __str__(self):
        propusk = '-------' * 20
        return f'Game : {self.name} /n price is {self.price}, /n image : {self.image}'


url = 'https://store.steampowered.com/search/?term='

response = requests.get(url)

soup = BeautifulSoup(response.text,'lxml')

games = soup.find_all('a')

for game in games:
    name = game.find('span', class_ = 'title')
    if name is not None:
        real_name = name.text
        image = game.find('img').get('src')
        price = game.find('div', class_ = 'discount_prices')
        if price is not None:
            price = price.text

        game = Game.from_soup(name, image, price)

        with open('movie.txt', 'a') as f:
            f.write(game.__str__())








