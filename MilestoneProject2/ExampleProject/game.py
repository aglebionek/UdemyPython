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
    #input() #uncomment to follow the game

    #each player plays a card
    card1 = player1.remove_card()
    card2 = player2.remove_card()

    #print(f'{card1} vs {card2}') #uncomment to follow the game

    #add the played cards to the pool (you can think of them as cards on table)
    cards_in_pool = [card1, card2]

    #check which card is greater rank-wise, suit doesn't matter in war. If any card is greater than the other, the player
    #who played the greater card gets all of the cards from the pool
    if card1 > card2:
        player1.add_cards(cards_in_pool)
        #print(f'Player1 won and has {player1.cards_left()}') #uncomment to follow the game 
    elif card2 > card1:
        player2.add_cards(cards_in_pool)
        #print(f'Player2 won and has {player2.cards_left()}') #uncomment to follow the game
    
    #if the cards are equal, then we have a war
    else:
        at_war = True
        #war can happen multiple times in a row, so we run the at_war loop for as long as someone wins it
        while at_war:
            #input() #uncomment to follow the game
            #print('War!') #uncomment to follow the game

            #for the sake of games not ending, a war forces a player to add 5 extra cards to the pool before resolving the war
            #we need to check if the player has that many cards to add to the pool. If he doesn't he looses.
            #even tho we add 5 cards to the pool, we need a player to have at least six, as the sixth will be the war resolving card
            if player1.cards_left() > 5:
                cards_in_pool.extend([player1.remove_card() for _ in range(5)]) # add five to pool
                card1 = player1.remove_card() # use the sixth for war resolving
                cards_in_pool.append(card1) # add it to the pool as well
            else:
                #print('Player one run out of cards for war and thus lost!') #uncomment to follow the game
                cards_in_pool.extend([player1.remove_card() for _ in range(player1.cards_left())]) # add the rest of the cards to the pool
                player2.add_cards(cards_in_pool) # I want the player to have all 52 cards after he wins
                at_war = False # no need for that, but it somehow bothers me if it remains true
                break
            if player2.cards_left() > 5:
                cards_in_pool.extend([player2.remove_card() for _ in range(5)])
                card2 = player2.remove_card()
                cards_in_pool.append(card2)
            else:
                #print('Player two run out of cards for war and thus lost!') #uncomment to follow the game
                cards_in_pool.extend([player2.remove_card() for _ in range(player2.cards_left())])
                player1.add_cards(cards_in_pool)
                at_war = False
                break

            #try to resolve the war
            if card1 > card2:
                player1.add_cards(cards_in_pool)
                #print(f'Player1 won and has {player1.cards_left()}') #uncomment to follow the game
                at_war = False
            elif card2 > card1:
                player2.add_cards(cards_in_pool)
                #print(f'Player2 won and has {player2.cards_left()}') #uncomment to follow the game
                at_war = False
            #if war isn't resolved, we simply stay in the war loop
            #else: #uncomment to follow the game
                #print('tie!') #uncomment to follow the game
        #print('End of war!') #uncomment to follow the game

#print out who won
if player1.cards_left() == 0: print('Player 2 won!')
else: print('Player 1 won!')