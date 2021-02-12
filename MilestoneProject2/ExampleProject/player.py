from typing import Union
from card import Card

class Player():
    def __init__(self, name: str) -> None:
        self.name = name
        self.cards = list()

    def remove_card(self) -> Card:
        return self.cards.pop(0)

    #The Union class allows to specify multiple input types
    def add_cards(self, cards: Union[list, Card]) -> None:
        if type(cards) == list:
            self.cards.extend(cards)
        else:
            self.cards.append(cards)

    def __str__(self) -> str:
        return f"Player {self.name} has {len(self.cards)}."

    
