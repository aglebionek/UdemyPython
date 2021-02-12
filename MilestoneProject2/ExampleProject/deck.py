from card import Card
import random

#I'm going to treat a list as a deck, with the right side of the list being the bottom of the deck, and the left side of the 
#list being the top of the deck
class Deck():
    def __init__(self) -> None:
        self.cards = list()

        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self) -> Card: return self.cards.pop(0)