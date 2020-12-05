class Animals:
    voice = ''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def talk(self):
        return print(f'{self.name} says \"{self.voice}!\"')

    def feed(self, food_weight):
        self.weight += food_weight
        return print(f'{self.name} eats {food_weight} kgs of food.')

class Milky(Animals):
    def milk(self):
        return print('milked')

class Cow(Milky):
    sound = 'moooo'

class Goat(Milky):
    sound = 'meee'

class Birds(Animals):
    def collect_eggs(self):
        return print('eggs collected')

class Duck(Birds):
    sound = 'crya'

class Goose(Birds):
    sound = 'gaaaa'

class Chicken(Birds):
    sound = 'chirick'

class Sheep(Animals):
    sound = 'beee'

    def shave(self):
        return print('wool collected.')

def create_farm():
    uncle_joe_farm = []
    uncle_joe_farm.append(Goose('Серый', 8))
    uncle_joe_farm.append(Goose('Белый', 9))
    uncle_joe_farm.append(Chicken('Ко-ко', 2))
    uncle_joe_farm.append(Chicken('Кукареку', 3))
    uncle_joe_farm.append(Sheep('Барашек', 15
    uncle_joe_farm.append(Sheep('Кудрявый', 12))
    uncle_joe_farm.append(Goat('Рога', 20))
    uncle_joe_farm.append(Goat('Копыта', 15))
    uncle_joe_farm.append(Cow('Манька', 400))
    uncle_joe_farm.append(Duck('Кряква', 7))

    def find_heaviest_animal():
        print(f'The heaviest animal is {sorted(uncle_joe_farm, key=lambda x: x.weight, reverse=True)[0].name}.')

    def find_total_weight():
        total_weight = 0
        for animal in uncle_joe_farm:
            total_weight += animal.weight
        print(f'Total weight of all the animals in the farm: {total_weight} kgs.')

    find_heaviest_animal()
    find_total_weight()

create_farm()