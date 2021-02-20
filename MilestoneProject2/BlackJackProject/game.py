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
    print('one card hidden')
    print(dealer.cards[1])
    print('\n')
    print("Player's hand: ")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    print("Dealer's hand: ")
    for card in dealer.cards:
        print(card)
    print('\n')
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
        pass
