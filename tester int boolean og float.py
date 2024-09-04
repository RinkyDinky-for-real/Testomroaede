import random
import blackjack_module as bjm


chips = 50

motstander_verdi = 0
kortstokk = list(bjm.get_new_shuffled_deck())

while True:
    spillerhånd = []
    motstandehånd = []

    spillerhånd.append(kortstokk.pop(0))
    spillerhånd.append(kortstokk.pop(0))

    motstandehånd.append(kortstokk.pop(0))
    motstandehånd.append(kortstokk.pop(0))

    spillerhånd_verdi = bjm.calculate_hand_value(spillerhånd)
    motstandehånd_verdi = bjm.calculate_hand_value(motstandehånd)


    print("spiller kort er:", spillerhånd, "med en totalverdi på", bjm.calculate_hand_value(spillerhånd))
    print("Motstander kort er:", motstandehånd[0], "med en totalverdi på", bjm.get_card_value(motstandehånd[0]))

    if bjm.calculate_hand_value(spillerhånd) == 21:
        print("Black_jack")
        break
    print(kortstokk)
    for x in range(len(kortstokk)):
        print(kortstokk[x])
    while True:#valg loop
        valg = input("ville du hit eller stand")
        if valg == "hit":
            spillerhånd.append(kortstokk.pop(0))
            print(spillerhånd)   
        if valg == "stand":
            while bjm.calculate_hand_value(motstandehånd) < 17:
                motstandehånd.append(kortstokk.pop(0))
            break
    print(motstandehånd)
    break   