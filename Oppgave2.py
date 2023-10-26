import random

class Card:
    card_count = 0

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.name = f'Card{Card.card_count}'
        Card.card_count += 1

    def __str__(self):
        return self.name

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
class Hand:
    def __init__(self):
        self.hands = ()
        pass
# Creating a deck, shuffling it, and drawing a card
idealdeck = Deck()
playdeck = list(idealdeck.cards)
player = Hand()
dealer = Hand()
def draw_card(x):
    if x:
        return x.pop()
    else:
        return None
card = draw_card(playdeck)
print(f"Drawn card: {card.rank} of {card.suit}")
playdeck = list(idealdeck.cards)
for card in playdeck:
    print(f"{card}: {card.rank} of {card.suit}")

