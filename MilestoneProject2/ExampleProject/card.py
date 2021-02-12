class Card():
    _VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
    'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
    SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str: return self.rank + " of " + self.suit

    def __gt__(self, card: 'Card') -> bool:
        return Card._VALUES[self.rank] > Card._VALUES[card.rank]

    def __eq__(self, card: 'Card') -> bool:
        return Card._VALUES[self.rank] == Card._VALUES[card.rank]

    def __lt__(self, card: 'Card') -> bool:
        return Card._VALUES[self.rank] < Card._VALUES[card.rank]