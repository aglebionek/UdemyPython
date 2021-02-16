from card import Card
class Hand:
    def __init__(self) -> None:
        self.cards = list()
        self.value = 0
        self.aces = 0

    def add_card(self, card: Card) -> None:
        self.cards.append(card)
        self.value += Card.VALUES[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        if self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1