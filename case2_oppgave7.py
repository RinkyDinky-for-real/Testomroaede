class Car:
    card_count = 0

    def __init__(self, brand, model, price, year, month, new, km):
        self.name = f"{brand.lower()}{model}"
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.month = month
        self.new = new
        self.km = km
    #her kan man se et lite mønster, de funksjonene som jeg legger til inni klasse-definisjonen er de kortere og simplere funksjonene, de som kan være litt ork å måtte calle, men de som man ikke trenger å forandre på så mye.
    def print_car_information(self):
        #kan være nyttig å ha her for å bare trenge å skrive car.print_car_information() for å få informasjon om bilen
    
    def is_new(self):
        #igjen, kan være nyttig å ha her, slik at man trenger bare å skrive car.is_new() for å få en boolean-verdi
    
    def get_car_age(self):
        #returnerer alderen til bilen, igjen, fin, kort funksjon som passer fint inni her
    
    def next_eu_control(self):
        #returnerer datoen for neste EU-kontroll, kan være nyttig å ha her

    
