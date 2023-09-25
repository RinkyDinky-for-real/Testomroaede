import random

dart_antall = [0, 0, 0]

player_score = []

player_antall = int(input("velg antall spillere"))

while len(player_score) < player_antall:
    player_score.append(int(0))

for n in range(len(player_score)):
    for i in range(len(dart_antall)):
        dart_antall[i] = random.randrange(0,61)
    player_score[n] = dart_antall[0]+dart_antall[1]+ dart_antall[2]
    print (f"Den totale poengsummen for spiller {n+1} ble: {player_score[n]}, med kastene: {dart_antall[0]},{dart_antall[1]},{dart_antall[2]}.")
