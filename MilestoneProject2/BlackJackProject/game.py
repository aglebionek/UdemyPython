# this is the codealong code, altho I don't like the code and there are some bugs:
# 1. if you play again your chips reset:
#    a method to empty hand would need to be created and the hands need to be instanciated only once
# 2. the question for playing again doesn't check if for incorrect answer
# 3. methods and variables names are kinda meh

from chips import Chips
from deck import Deck
from hand import Hand

def take_bet(chips: Chips) -> None:
    while True:
        try: chips.bet = int(input('How many chips would you like to bet? '))
        except: print('Sorry, please provide an integer')
        else:
            if chips.bet > chips.total: print(f'Sorry, you don\'t have enough chips! You have {chips.total}')
            else: break

def hit(deck: Deck, hand: Hand) -> None:
    card = deck.deal_one()
    hand.add_card(card)
    hand.adjust_for_ace()

def hit_or_stand(deck: Deck, hand: Hand) -> None:
    global playing
    while True:
        x = input('Hit or Stand? (h/s)')
        if x[0].lower() == 'h': hit(deck, hand)
        elif x[0].lower() == 's': 
            print('Player stands dealer turn')
            playing = False
        else:
            print("Please enter either 'h' or 's'.")
            continue
        break

def show_some(player: Hand, dealer: Hand) -> None:
    print("Dealer's hand: ")
    print(dealer.cards[1])
    print('one card hidden')
    print("Player's hand: ")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    print("Dealer's hand: ")
    for card in dealer.cards:
        print(card)
    print("Player's hand: ")
    for card in player.cards:
        print(card)

def player_busts(player: Hand, dealer: Hand, chips: Chips) -> None:
    print('Player busts')
    chips.lose_bet()

def player_wins(player: Hand, dealer: Hand, chips: Chips) -> None:
    print('Player wins')
    chips.win_bet()

def dealer_busts(player: Hand, dealer: Hand, chips: Chips) -> None:
    print('Dealer busts')
    chips.win_bet()

def dealer_wins(player: Hand, dealer: Hand, chips: Chips) -> None:
    print('Dealer wins')
    chips.lose_bet()

def push(player: Hand, dealer: Hand):
    print('Dealer and player tie! PUSH')

while True:
    print('Welcome to Blackjack')
    playing = True
    deck = Deck()
    deck.shuffle()

    player = Hand()
    player.add_card(deck.deal_one())
    player.add_card(deck.deal_one())

    dealer = Hand()
    dealer.add_card(deck.deal_one())
    dealer.add_card(deck.deal_one())

    player_chips = Chips()
    take_bet(player_chips)
    show_some(player, dealer)

    while playing:
        hit_or_stand(deck, player)
        show_some(player, dealer)
        
        if player.value > 21:
            player_busts(player, dealer, player_chips)
            break

    if player.value <= 21:
        while dealer.value < 17: hit(deck, dealer)
        
        show_all(player, dealer)

        if dealer.value > 21: dealer_busts(player, dealer, player_chips)
        elif dealer.value > player.value: dealer_wins(player, dealer, player_chips)
        elif dealer.value < player.value: player_wins(player, dealer, player_chips)
        else: push(player, dealer)
    
    print(f'\n Player total chips are at: {player_chips.total}')
    
    new_game = input('Would you like to play another hand? (y/n)')
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for playin!')
        break
