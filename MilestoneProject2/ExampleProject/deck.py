from card import Card
import random

class Deck():
    def __init__(self) -> None:
        self.all_cards = list()

        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self) -> None:
        random.shuffle(self.all_cards)

deck = Deck()
deck.shuffle()
for card in deck.all_cards:
    print(card)