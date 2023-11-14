from datetime import date
car_register = {
    "toyotaBZ4X": {
        "brand": "Toyota",
        "model": "Corolla",
        "price": 96_000,
        "year": 2012,
        "month": 8,
        "new": False,
        "km": 163_000
        },
    "pugeot408": {
        "brand": "Pugeot",
        "model": "408",
        "price": 330_000,
        "year": 2019,
        "month": 1,
        "new": False,
        "km": 40_000
        },
    "audiRS3": {
        "brand": "Audi",
        "model": "RS3",
        "price": 473_000,
        "year": 2022,
        "month": 2,
        "new": True,
        "km": 0
        },
    }
NEW_CAR_REGISTRATION_FEE = 8745
RENT_CAR_PERCENTAGE = 0.4
RENT_NEW_CAR__FEE = 1000
def print_car_information(car):
    print(f"Brand: {car['brand']}")
# Oppgave 3.1
def create_car(car_register, brand, model, price, year, month, new, km):
    print(f"Car created: {brand} {model}")
# Oppgave 3.2
def get_car_age(car):
    print(f"Car age: {car_age} years and {car_age_months} months")
# Oppgave 3.3
def next_eu_control(car):
    print(f"Next EU-control: {next_eu_control_date}")
# Oppgave 3.4
def rent_car_monthly_price(car):
    print(f"Monthly price: {monthly_price}")
# Oppgave 3.5
def calculate_total_price(car):
    print(f"Total price: {total_price}")
# Oppgave 3.6
def is_new(car):
    return car['new']

if __name__ == '__main__':
    create_car(car_register, "Volvo", "V90", 850_000, 2021, 12, True, 0)
    toyota = car_register['toyotaBZ4X']
    print_car_information(toyota)
    
    print(f"\nThe total price for this {toyota['brand']} {toyota['model']} is {calculate_total_price(toyota)}kr.")
    
    print(f"Next EU-control for the {toyota['brand']} {toyota['model']} is {next_eu_control(toyota)}")
    
    print(f"If you want to rent the {toyota['brand']} {toyota['model']} the monthly fee will be {rent_car_monthly_price(toyota)}.")
    
    audi = car_register['audiRS3']
    
    print_car_information(audi)
    print(f"\nThe total price for this {audi['brand']} {audi['model']} is {calculate_total_price(audi)}kr.")
    print(f"Next EU-control for the {audi['brand']} {audi['model']} is {next_eu_control(audi)}")
    print(f"If you want to rent the {audi['brand']} {audi['model']} the monthly fee will be {rent_car_monthly_price(audi)}kr.")