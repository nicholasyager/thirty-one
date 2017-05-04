import random
import itertools

class Card:
    points = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 10,
            'Q': 10,
            'K': 10,
            'A': 11
        }

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        self.score = self.points[self.face]

    def __repr__(self):
        return self.face + self.suit

class Deck:

    def __init__(self):
        self.suits = ['♦', '♥', '♣', '♠']
        self.cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q',
                      'K', 'A']
        self.deck = [Card(item[0], item[1]) for item in 
                        itertools.product(self.cards, self.suits)]

        random.shuffle(self.deck)

    def __repr__(self):
        return ', '.join(map(str, self.deck))

def main():
    deck = Deck()
    print(deck)



if __name__ == "__main__":
    main()
