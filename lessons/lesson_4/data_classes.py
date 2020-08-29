from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str

class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

cards = [
    DataClassCard('Q', 'Hearts'),
    RegularCard('Q', 'Hearts')
]

if __name__ == '__main__':
    print("Let's compare DataClass to RegularClass\n")
    for card in cards:
        print(card.__class__.__name__)
        print('-----' * 5)

        print(f'card rank: {card.rank}')
        print(card)

        equality = card == type(card)('Q', 'Hearts')
        print(f'Equality test: {equality}')
        print('\n')