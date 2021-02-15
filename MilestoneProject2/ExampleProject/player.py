from card import Card
from typing import Union

class Player():
    def __init__(self, name: str) -> None:
        '''
        A player class, can hold, draw and play cards.
        '''
        self.name = name
        self.cards = list()

    def remove_card(self) -> Card:
        '''
        Return and remove a card from the top of player's cards.
        '''
        return self.cards.pop(0)

    #The Union class allows to specify multiple input types
    def add_cards(self, cards: Union[list, Card]) -> None:
        '''
        Add either a single card or a list of cards to the bottom of player's deck.
        '''
        if type(cards) == list:
            #Case for adding multiple cards
            self.cards.extend(cards)
        else:
            #Case for adding one card
            self.cards.append(cards)

    def cards_left(self) -> int:
        '''
        Returns the number of cards in player's hand.
        '''
        return len(self.cards)

    def __str__(self) -> str:
        return f"Player {self.name} has {len(self.cards)}."

    
