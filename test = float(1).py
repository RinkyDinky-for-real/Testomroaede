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
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

deck = Deck()
random.shuffle(deck.cards)

def draw_card(x):
    if x:
        return x.pop()
    else:
        return None
card = draw_card(deck.cards)
print(f"Drawn card: {card}: {card.rank} of {card.suit}")

#print(deck.cards)
# You can continue drawing cards until the deck is empty.
