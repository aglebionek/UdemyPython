from card import Card
from random import shuffle as randomshuffle

#I'm going to treat a list as a deck, with the right side of the list being the bottom of the deck, and the left side of the 
#list being the top of the deck
class Deck():
    def __init__(self) -> None:
        '''
        A class that implements basic functionality of a deck of cards. A new instance contains all the cards without the jokers, sorted by suit and then by rank.
        '''
        self.cards = list()

        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self) -> None:
        '''
        Shuffles the deck.
        '''
        randomshuffle(self.cards)

    def deal_one(self) -> Card:
        '''
        Removes and returns the top card from the deck.
        '''
        return self.cards.pop(0)

    def __len__(self) -> int:
        '''
        Returns the number of cards left in the deck.
        '''
        return len(self.cards)