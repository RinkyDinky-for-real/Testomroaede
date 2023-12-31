import random


class Card:  # lager card class
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
        ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
                 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))  # lager alle kortene


class Hand:
    def __init__(self, x):
        self.name = x
        self.hands = []
        self.value = int(0)
        self.result = ""  # må lagre verdier, stussa virkelig på hvorfor ingenting funka, helt til chatgpt forklarte det elementære til meg
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
chips = 10  # disse kunne ha blitt flyttet inn i Hand-klassen, så hadde det vært mye lettere å få til EVT flerspillere
wager = 0
gameOver = False
player_played = False
idealdeck = Deck()
playdeck = list(idealdeck.cards)
outcome = ""  # lagringggggg
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


def sum_hand(x):  # chatgpt hjalp meg her
    x.value = 0
    x.has_ace = False
    for card in x.hands:
        x.value += rank_value(card.rank)
        if card.rank == "Ace":
            x.has_ace = True
    if x.has_ace and x.value <= 11:  # sjekker om ess må være 11 eller 1
        x.value += 10
    return x.value


def sum_hand_dealer(x):  # chatgpt hjalp meg her
    x.value = 0
    x.has_ace = False
    d_card = x.hands[0]
    if d_card:
        x.value += rank_value(d_card.rank)
        if d_card.rank == "Ace":
            x.has_ace = True
    if x.has_ace and x.value <= 11:  # sjekker om ess må være 11 eller 1
        x.value += 10
    return x.value


def showhand(x):#printer hånden
    print(f"The {x.name}'s hand consists of the following cards: ")
    for card in x.hands:
        print(f"{card.rank} of {card.suit}")
    print(f"For a combined value of: {sum_hand(x)}")


def showhand_dealer(x):#for å vise dealeren sitt synlige kort
    print(f"The {x.name}'s visible card is: ")
    d_card = x.hands[0]# chat hjalp meg her
    if d_card:
        print(f"{d_card.rank} of {d_card.suit}")
    print(f"For a value of: {sum_hand_dealer(x)}")


def chipswager(x):
    global wager
    while True:
        wager = int(
            input(f"You have {x} chip(s) remaining, how many do you want to bet?"))
        if wager > x:
            print("You can't bet more than you have!")
        elif wager < x:
            print(f"You have decided to bet {wager} chip(s)")
            break
        elif wager == x:
            print("All in? Gutsy.")
            break


def gamesetup():
    global playdeck
    global player_played
    player.hands.clear()
    dealer.hands.clear()
    player.has_ace = False
    dealer.has_ace = False
    player_played = False
    playdeck = list(idealdeck.cards)
    random.shuffle(playdeck)
    draw_to_hand(draw_card(playdeck), player)
    draw_to_hand(draw_card(playdeck), player)
    draw_to_hand(draw_card(playdeck), dealer)
    draw_to_hand(draw_card(playdeck), dealer)
    chipswager(chips)
    showhand(player)
    showhand_dealer(dealer)


def player_turn():
    global gameOver
    global player_played
    global dealer
    if len(player.hands) == 2 and sum_hand(player) == 21:
        print("Player has a Blackjack! Now to see what the dealer has.....")
        player_played = True
        return "blackjack"
    while player_played == False:
        decision = input(
            "Do you want to hit or stand? Enter 'h' for hit or 's' for stand: ").lower()

        if decision == "h":
            # får kort
            draw_to_hand(draw_card(playdeck), player)
            showhand(player)
            showhand_dealer(dealer)

            # ambasing
            if sum_hand(player) > 21:
                print("Player busts! You lose.")
                player_played = True
                return "bust"
        if len(player.hands) > 2 and sum_hand(player) == 21:
            # lar deg ikke throwe
            print("Player has 21!")
            player_played = True
            return ("stand")
        elif decision != "h" and decision != "s":
            print("Invalid input. Please enter 'h' for hit or 's' for stand.")
        elif decision == "s":
            player_played = True
            return ("stand")


def dealer_turn():
    if len(dealer.hands) == 2 and sum_hand(dealer) == 21:
        print("Dealer has a Blackjack!")
        return "blackjack"
    while sum_hand(dealer) < 17:
        # dealer spiller
        draw_to_hand(draw_card(playdeck), dealer)
    showhand(dealer)
    if sum_hand(dealer) > 21:
        print("Dealer busts!")
        return "bust"


def game_outcome():  # om du vinner eller taper
    if player.result == "blackjack" and dealer.result == "blackjack":
        return "pushbyblackjack"
    elif player.result == "blackjack":
        return "blackjack"
    elif dealer.result == "blackjack":
        return "lossbyblackjack"
    elif player.result == "bust":
        return "lossbybust"
    elif dealer.result == "bust":
        return "win"
    elif sum_hand(player) == sum_hand(dealer):
        return "push"
    elif sum_hand(player) > sum_hand(dealer):
        return "win"
    else:
        return "loss"


def update_chips():
    global outcome
    global chips
    global wager  # mr worldwide
    if outcome == "win":
        chips += wager
    elif outcome == "loss":
        chips -= wager
    elif outcome == "lossbybust":
        chips -= wager
    elif outcome == "lossbyblackjack":
        chips -= wager
    elif outcome == "push":
        chips = chips
    elif outcome == "pushbyblackjack":
        chips = chips
    elif outcome == "blackjack":
        chips += (wager*2)


def results(x):  # printer fancy ting i terminalen
    global outcome
    if outcome == "win":
        print("You win! Very nice!")
    elif outcome == "loss":
        print("You lose! Better luck next time....")
    elif outcome == "lossbyblackjack":
        print("You lose to blackjack! Unlucky! Better luck next time....")
    elif outcome == "lossbybust":
        print("You lose by busting! Unlucky! Better luck next time....")
    elif outcome == "push":
        print("Push! Nobody wins....")
    elif outcome == "push":
        print("Push by blackjack! Unlucky, or lucky, you decide....")
    elif outcome == "blackjack":
        print("You win by blackjack! Very nice!")
    print(f"As a result of the game, you now have {x} chip(s) remaining.")


def check_if_game_over(x):
    global gameOver
    if x <= 0:
        print("You are destitute! You lose........")
        gameOver = True


def play_again():
    while not gameOver:
        # GPT ga meg ideen om å legge til lower for å gjøre alt smått
        choice = input(
            "do you want to play again? 'y' for yes, 'n' for no.").lower()
        if choice == "y":
            print(
                "You have chosen to play again. the code will now reset your hands and shuffle the cards......")
            return "playagain"
        elif choice == "n":
            print("You have chosen to not play again. Au revoir....")
            return "notagain"
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")


while not gameOver:  # gameloop
    gamesetup()
    player.result = player_turn()
    dealer.result = dealer_turn()
    outcome = game_outcome()
    update_chips()
    results(chips)
    check_if_game_over(chips)
    choice = play_again()
    if choice == "playagain":
        continue
    elif choice == "notagain":
        break
    else:
        Exception(
            "something has gone REALLY wrong here, please restart the program")
