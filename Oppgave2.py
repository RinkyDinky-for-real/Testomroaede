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
                self.cards.append(Card(rank, suit))#lager alle kortene
class Hand:
    def __init__(self, x):
        self.name = x
        self.hands = []
        self.value = int(0)
        self.result = ""
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
chips = 7 #disse kunne ha blitt flyttet inn i Hand-klassen, så hadde det vært mye lettere å få til EVT flerspillere 
wager = 0
gameOver = False

idealdeck = Deck()
playdeck = list(idealdeck.cards)
random.shuffle(playdeck)
player = Hand("player")
dealer = Hand("dealer")

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
    x.value = 0
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
def chipswager(x):
    global wager
    while True:
        wager = int(input(f"You have {x} chip(s) remaining, how many do you want to bet?"))
        if wager > x:
            print("You can't bet more than you have!")
        else:
            print(f"You have decided to bet {wager} chip(s)")
            break  # Exit the loop when a valid wager is made
def gamesetup():
    draw_to_hand(draw_card(playdeck), player)
    draw_to_hand(draw_card(playdeck), player)
    draw_to_hand(draw_card(playdeck), dealer)
    draw_to_hand(draw_card(playdeck), dealer)
    chipswager(chips)
    showhand(player)
    showhand_dealer(dealer)
#den skitten som funker^ 
#den skitten som ikke funker smh smh
def player_turn():
    global gameOver
    if len(player.hands) == 2 and sum_hand(player) == 21:
            print("Player has a Blackjack! Now to see what the dealer has.....")
            return "blackjack"
    while True:
        decision = input("Do you want to hit or stand? Enter 'h' for hit or 's' for stand: ").lower()
        
        if decision == "h":
            # Player chooses to hit
            draw_to_hand(draw_card(playdeck), player)
            showhand(player)

            # Check if the player busts (hand value exceeds 21)
            if sum_hand(player) > 21:
                print("Player busts! You lose.")
                return "bust"
        if len(player.hands) > 2 and sum_hand(player) == 21:
            # Player reached 21 after hitting with more than two cards.
            print("Player has 21! Your turn ends.")
            return("stand")
        elif decision != "h" and decision != "s":
            print("Invalid input. Please enter 'h' for hit or 's' for stand.")
        elif decision == "s":
            return("stand")
def dealer_turn():
    if len(dealer.hands) == 2 and sum_hand(dealer) == 21:
            print("Dealer has a Blackjack!")
            return "blackjack"
    while sum_hand(dealer) < 17:
        # Dealer must hit until the hand value is 17 or greater
        draw_to_hand(draw_card(playdeck), dealer)
    showhand(dealer)
    if sum_hand(dealer) > 21:
                print("Dealer busts!")
                return "bust"

def game_outcome():
    if player.result == "bust":
        return "loss"
    elif dealer.result == "bust":
        return "win"
    elif sum_hand(player) == sum_hand(dealer):
        return "push"
    elif player.result == "blackjack" and dealer.result == "blackjack":
        return "push"
    elif player.result == "blackjack":
        return "blackjack"
    elif dealer.result == "blackjack":
        return "loss"
    elif sum_hand(player) > sum_hand(dealer):
        return "win"
    else:
        return "loss"
    
while not gameOver:#gameloop
    if chips <= 0:
        print("You are destitute!")
        gameOver = True
        break
    
    # Game setup (deal cards and place a wager)
    gamesetup()
    
    # Player's turn
    player.result = player_turn()  # Implement player's decision (hit or stand)
    
    # Dealer's turn
    dealer.result = dealer_turn()  # Implement dealer's decision (hit or stand)

    # Determine the game outcome
    game_outcome()  # Example: win, lose, or push
    print(game_outcome())
    print(player_turn())
    break
    # Update chips and check for game over conditions
    #update_chips()  # Example: adjust chips based on game outcome and check if the player wants to continue

# End of game loop