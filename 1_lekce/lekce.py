
sausages = {"Jirka": 2, "Naty": 1, "Adam": 4, "Lucka": 2, "Pavča": 2}
sausages["Naty"] = 0
sausages.pop("Naty")
print(len(sausages))

#1.priklad
vysvedceni = {"cestina": 1, "matika": 2, "dejepis": 5}
print(vysvedceni)

#2.priklad
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
sales["Noc, která mě zabila"] = 0
sales ["Vrah zavolá v deset"] += 100
print(sales)

##.priklad
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
cislolistku = int(input('Zadej cislo listku'))
if cislolistku in tombola:
    print ('Vyhravas', tombola[cislolistku], '.')
else:
    print ('Nevyhravas.')