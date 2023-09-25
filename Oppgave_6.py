pakke_list = []
while True:
    valg = input("Velg en handling, velg mellom legg til, slett, print og avslutt:")
    if valg == "legg til":
        item = input("Hva vil du legge til i listen?:")
        pakke_list.append(item)
    if valg == "slett":
        item = input("Hva vil du slette fra listen?:")#her må man skrive inn hva man vil slette, ikke nummeret på item i lista!
        pakke_list.remove(item)
    if valg == "print":
        print("Her er din liste, som den ser ut nå:")
        for i in pakke_list:
            print(i)
    if valg == "avslutt":
        last_chance = input("Du har valgt å avslutte, har du lyst til å se på listen en siste gang?:")
        if last_chance == "ja":
            for i in pakke_list:
                print(i)
            print("Hadet!")
        else:
            print("Neivel, hadet!")
        break