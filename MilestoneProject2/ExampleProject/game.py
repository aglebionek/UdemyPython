from card import Card
from deck import Deck
from player import Player

#Instanciate two players
player1 = Player('Mano')
player2 = Player('Sia')

#Instantiate a deck and shuffle it
deck = Deck()
deck.shuffle()

#Deal cards to players from the deck until there is no more cards in the deck
left_in_deck = len(deck)
while left_in_deck > 0:
    if left_in_deck % 2 == 0: player1.add_cards(deck.deal_one())
    else: player2.add_cards(deck.deal_one())
    left_in_deck -= 1

while player1.cards_left() > 0 and player2.cards_left() > 0:
    break