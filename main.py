# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("Těším se na dlouhodobý kurz :-) :-)")

item = {"title": "Čajová konvička s hrnky", "price": 899, "inStock": True}
key = "price"
item[key] = 929
print("Vybraný předmět je " + item["title"] + " a cena je " + str(item["price"]) + ".")
print("Vybraný předmět je", item["title"], "a cena je", item["price"],".")
print(f"Vybraný předmět je {item['title']} a cena je {item['price']}.")
item["weight"] = 0.6
if "weight" in item:
    print(f"Hmotnost předmětu je {item['weight']}")
else:
    print("Hmotnost není zadána.")

# prvni příklad
vysvedceni = {"matematika": 1, "anglictina": 3, "dejepis": 2}
print(vysvedceni)

# druhy příklad
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
sales["Noc, která mě zabila"] = 0
sales["Vrah zavolá v deset"] += 10
print (sales)
print(sales["Vrah zavolá v deset"])

# třetí příklad
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
listek = int(input('Zadej cislo listku:'))

if listek in tombola:
    print('Vyhravas:', tombola[listek])
    tombola.pop(listek)
else:
    print('Nevyhravas')
