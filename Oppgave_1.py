tall = int(input("Hva er svaret på det ultimate spørsmålet om livet, universet og alle ting? Hint: Det er et tall."))

if tall == 42:
    print("Det stemmer, meningen med livet er 42!")
elif tall > 30 and tall < 50:
    print("Nærme, men feil.")
else:
    print("FEIL")
