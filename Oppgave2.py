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
    def __init__(self, x):
        self.name = x
        self.hands = []
        self.value = int(0)
        self.has_ace = False
values = {
    'Ace': 1,  # Ess håndteres inni funksjonen
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10
}
def rank_value(rank):
    return values[rank]
def draw_card(x):
    if x:
        return x.pop()
    else:
        return None
def draw_to_hand(x, y):
    if x:
        y.hands.append(x)
def sum_hand(x):
    for card in x.hands:
        x.value += rank_value(card.rank)
        if card.rank == "Ace":
            x.has_ace = True
    if x.has_ace and x.value <= 11: #sjekker om ess må være 11 eller 1
        x.value += 10  
    return x.value
def sum_hand_dealer(x):
    d_card = x.hands[0]
    if d_card:
        x.value += rank_value(d_card.rank)
        if d_card.rank == "Ace":
            x.has_ace = True
    if x.has_ace and x.value <= 11: #sjekker om ess må være 11 eller 1
        x.value += 10  
    return x.value
def showhand(x):
    print(f"The {x.name}'s hand consists of the following cards:")
    for card in x.hands:
        print(f"{card.rank} of {card.suit}")
    print(f"For a combined value of:{sum_hand(x)}")
def showhand_dealer(x):
    print(f"The {x.name}'s visible card is:")
    d_card = x.hands[0]
    if d_card:
        print(f"{d_card.rank} of {d_card.suit}")
    print(f"For a value of:{sum_hand_dealer(x)}")
chips = 7
wager = 0
gameOver = False

idealdeck = Deck()
playdeck = list(idealdeck.cards)
random.shuffle(playdeck)
player = Hand("player")
dealer = Hand("dealer")

draw_to_hand(draw_card(playdeck), player)
draw_to_hand(draw_card(playdeck), player)
draw_to_hand(draw_card(playdeck), dealer)
draw_to_hand(draw_card(playdeck), dealer)
showhand(player)
showhand_dealer(dealer)
#while gameOver == False:#gameloop
#    print()