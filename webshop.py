def print_ware_information(ware):#oppgave 1
    #Funksjonsbeskrivelse: Printer ut informasjon om en spesifisert vare.
    print(f"Name: {ware['name']}")
    print(f"Price: {ware['price']},-")
    print(f"Number in stock: {ware['number_in_stock']}")
    print(f"Description: {ware['description']}")
    print("************************************")

def calculate_average_ware_rating(ware):#oppgave 2
    ratings = ware["ratings"]
    try:
        return round(sum(ratings) / len(ratings), 1)
    except ZeroDivisionError:
        print("There are no ratings for this product.")
        return 0
def get_all_wares_in_stock(all_wares):#oppgave 3
    #Returnerer en liste med alle varer som er på lager.
    wares_in_stock = {}
    for key, value in all_wares.items():
        if is_ware_in_stock(value):
            wares_in_stock[key] = value
    return wares_in_stock


def is_number_of_ware_in_stock(ware, number_of_ware):#oppgave 4
    #Returnerer en Boolean-verdi som representerer om et spesifisert antall av en gitt vare finnes på lager.
    return ware['number_in_stock'] >= number_of_ware
def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware=1):#oppgave 5
    # Legger til et spesifisert antall av en gitt vare i en spesifisert handlevogn.
    if is_ware_in_stock(ware) == False:
        print(f"{ware['name']} is out of stock.")
    
    elif is_number_of_ware_in_stock(ware, number_of_ware) == True:
        shopping_cart[ware_key] = number_of_ware
        print(f"{number_of_ware} {ware['name']} added to the shopping cart.")
    
    elif is_number_of_ware_in_stock(ware, number_of_ware) == False:
        print(f"Only {ware['number_in_stock']} {ware['name']} in stock.")
        print(f"All {ware['number_in_stock']} {ware['name']} in stock added to the shopping cart.")
        shopping_cart[ware_key] = ware['number_in_stock']

def calculate_shopping_cart_price(shopping_cart, all_wares, tax=1.25):#oppgave 6
    #Returnerer prisen av en handlevogn basert på varene i den.
    total_price = 0
    for ware_key, amount in shopping_cart.items():
        if ware_key in all_wares:
            ware = all_wares[ware_key]
            price = ware["price"]
            total_price += price * amount
        else:
            print(f"{ware_key} is not a valid ware key.")
    total_price_with_tax = total_price * tax
    return total_price_with_tax

def can_afford_shopping_cart(shopping_cart_price, wallet):#oppgave 7
    #Returnerer en Boolean-verdi basert på om det er nok penger i en gitt lommebok for å kjøpe en handlevogn.
    if wallet.get_amount() >= shopping_cart_price:
        return True
    else:
        return False
def buy_shopping_cart(wallet, shopping_cart, all_wares):#oppgave 8
    print("************************************")
    print("Attempting to buy shopping cart...")
    print("************************************")
    for key, value in shopping_cart.items():
        if key in all_wares and all_wares[key]["number_in_stock"] >= value:
            all_wares[key]["number_in_stock"] -= value
            shopping_cart[key] = value
            print(f"{value} {all_wares[key]['name']} bought.")
        elif key in all_wares and all_wares[key]["number_in_stock"] < 1:
            shopping_cart.pop(key)
            print(f"{all_wares[key]['name']} is out of stock.")
            break#slik at det ikke kræsjer når det er tomt for en vare
        elif key in all_wares and all_wares[key]["number_in_stock"] < value:
            shopping_cart[key] = all_wares[key]["number_in_stock"]
            all_wares[key]["number_in_stock"] = 0
            print(f"Not enough of {all_wares[key]['name']} in stock.")
            print(f"Instead, all {shopping_cart[key]} of {all_wares[key]['name']} will be bought.")
        else:
            continue
    print("************************************")
    print(f"The total price of the wares after tax was: {calculate_shopping_cart_price(shopping_cart, all_wares)}kr.")
    for key, value in shopping_cart.items():
        if all_wares[key]["number_in_stock"] > 0:
            shopping_cart[key] = value if value <= all_wares[key]["number_in_stock"] else all_wares[key]["number_in_stock"]
    if can_afford_shopping_cart(calculate_shopping_cart_price(shopping_cart, all_wares), wallet):
        wallet.subtract_amount(calculate_shopping_cart_price(shopping_cart, all_wares))
        clear_shopping_cart(shopping_cart)
        print("The purchase was successful.")

#------------------------------------------
# Predefinerte funksjoner
#------------------------------------------
def is_ware_in_stock(ware):
    #Returnerer en Boolean-verdi som representerer om en vare er på lager.
    if ware["number_in_stock"] >= 1:
        return True
    else:
        return False
def clear_shopping_cart(shopping_cart):
    #Tømmer en handlevogn.
    shopping_cart.clear()