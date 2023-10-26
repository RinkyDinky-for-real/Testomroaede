#Vet ikke om dette var riktig måte å gjøre denne oppgaven på......
def volum_calc(x,y,z):
    volum = int(x*y*z)
    print(f"Volumet er {volum} cm³.")

while True:
    if input("Vil du kjøre funksjonen? Y/N") == "Y":
        x = int(input("Hva er lengden på objektet i cm?"))
        y = int(input("Hva er bredden på objektet i cm?"))
        z = int(input("Hva er høyden på objektet i cm?"))
        volum_calc(x, y, z)
    else:
        print("Neivel")