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
def print_car_information(car):# Oppgave 3.1
    if is_new(car):
        print(f"Brand: {car['brand']}, Model: {car['model']}, Price: {car['price']}, Year: {car['year']}, Month: {car['month']}, Condition: New, Mileage: {car['km']} Km.")
    else:
        print(f"Brand: {car['brand']}, Model: {car['model']}, Price: {car['price']}, Year: {car['year']}, Month: {car['month']}, Condition: Used, Mileage: {car['km']} Km.")
def create_car(car_register, brand, model, price, year, month, new, km):# Oppgave 3.2
    car_id = f"{brand.lower()}{model}"
    car = {
        "brand": brand,
        "model": model,
        "price": price,
        "year": year,
        "month": month,
        "new": new,
        "km": km
    }
    car_register[car_id] = car

def get_car_age(car):# Oppgave 3.3
    car_age = date.today().year - car['year']
    return car_age
def rent_car_monthly_price(car):# Oppgave 3.4
    monthly_price = (car['price'] * RENT_CAR_PERCENTAGE)/12
    if car['new'] == True:
        monthly_price += RENT_NEW_CAR__FEE
    monthly_price = round(monthly_price, 2)
    return monthly_price
def next_eu_control(car):# Oppgave 3.5
    logic_year = car['year']
    while True:
        logic_year += 2
        if logic_year > date.today().year:
            break
        if logic_year < date.today().year:
            continue
    next_eu_control_date = date(logic_year, car['month'], 1)
    return next_eu_control_date
def calculate_total_price(car):# Oppgave 3.6
    car_price = int(car['price'])
    if car['new'] == True:
        car_price += NEW_CAR_REGISTRATION_FEE
    elif get_car_age(car) in range(0, 4):
        car_price += 6681
    elif get_car_age(car) in range(3, 12):
        car_price += 4034
    elif get_car_age(car) in range(11, 30):
        car_price += 1729
    elif get_car_age(car) > 30:
        car_price += 0
    return car_price

def is_new(car):
    return car['new']

if __name__ == '__main__':
    create_car(car_register, "Volvo", "V90", 850_000, 2021, 12, True, 0)
    toyota = car_register['toyotaBZ4X']
    print_car_information(toyota)

    print(f"\nThe total price for this {toyota['brand']} {toyota['model']} is {calculate_total_price(toyota)}kr.")
    print(f"age: {get_car_age(toyota)}")
    print(f"Next EU-control for the {toyota['brand']} {toyota['model']} is {next_eu_control(toyota)}")
    
    print(f"If you want to rent the {toyota['brand']} {toyota['model']} the monthly fee will be {rent_car_monthly_price(toyota)}.")
    
    audi = car_register['audiRS3']
    
    print_car_information(audi)
    print(f"\nThe total price for this {audi['brand']} {audi['model']} is {calculate_total_price(audi)}kr.")
    print(f"Next EU-control for the {audi['brand']} {audi['model']} is {next_eu_control(audi)}")
    print(f"If you want to rent the {audi['brand']} {audi['model']} the monthly fee will be {rent_car_monthly_price(audi)}kr.")