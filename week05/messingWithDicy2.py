# Messing with Dictionaries 2
# Author: Tihana Gray

car = {
    "make": "Fiat",
    "model": "Punto",
    "price": 10000,
    "tags": ["pre-owned", "best-buy", "Dealer"],
}

# print (car)

# for key in car:
#    print (key, 'has value', car[key])

for key, value in car.items():
    print (key, 'has value', value)