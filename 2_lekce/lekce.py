sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
print ('Vydane knizky:')
for key in sales:
    print(key)

#vypise klice, vzdy vypisuje key ne ten cely slovnik

#kdyz chci vypsat dve promenne
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
print ('Vydane knizky:')
for key, value in sales.items(): #pochopi diky tomi item ze ma vzit oboji
    print('Knihy', (key), 'se prodalo', (value), 'kusu.')

#s pridanim vypoctu celkove hodnoty
total = 0
print ('Vydane knizky:')
for key, value in sales.items(): #pochopi diky tomi item ze ma vzit oboji
    print('Knihy', (key), 'se prodalo', (value), 'kusu.')
    total += value
print('Celkem bylo prodano', (total), '.')

#SEZNAM ktery se sklada z jednotlivych slovniku
books = [
  {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
  {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
  {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]
total = 0
for item in books: #neni tu item protoze je to seznam ne slovnik
    total += item["sold"] * item["price"]
print('Celkove trzby jsou ', (total), '.')

# pricitat jenom nektere knizky
books = [
  {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
  {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
  {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]
total = 0
for item in books: #neni tu item protoze je to seznam ne slovnik
    if item["year"] == 2019:
        total += item["sold"] * item["price"]
print('Celkove trzby jsou ', (total), '.')

# Čtenářský deník
# Gustav je vášnivým čtenářem detektive z našeho nakladatelství a navíc si zapisuje knihy, které přečetl. Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.
#
# Napiš program, který spočte celkový počet stran, které Gustav přečetl.
# Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.

books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]
stranycelkem = 0
for item in books:
    if item["rating"] > 8:
        stranycelkem += item["pages"]
print('Celkem precetl', (stranycelkem), '.')
print ('Precetl celkem',(len(item)), 'knihy.')

# Vysvědčení
# Uvažujme vysvědčení, které máme zapsané jako slovník.
#
# Napiš program, který spočte průměrnou známku ze všech předmětů.
# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.

schoolReport = {
  "Český jazyk": 1,
  "Anglický jazyk": 1,
  "Matematika": 1,
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělešná výchova": 3,
  "Chemie": 4,
}

submark = 0
for subject, mark in schoolReport.items():
    submark += mark
    if mark ==1:
        print (subject, end='/ ') #nebude vzpisovat na nove radky ale bude psat lomitko

print(submark/len(schoolReport))

# Poznávací značky
# V následujícím slovníků je evidence automobilů. Klíčem jsou státní poznávací značky (SPZ) a hodnotou je jméno majitele vozu. Napiš program, který vypíše všechny majitele, jejichž vozidlo je registrováno v Plzňském kraji, tj. na druhém místě (index 1!) řetězce v klíči je písmeno P.

plates = {"4A2 3000": "František Novák",
  "6P5 4747": "Jana Pilná",
  "3B7 3652": "Jaroslav Sečkár",
  "1P5 5269": "Marta Nováková",
  "37E 1252": "Martina Matušková",
  "2A5 2241": "Jan Král"}

for spz, majitel in plates.items():
    if spz[1] == 'P': #prvni hodnota je na nultem listi, proto se pise jednicka
        print(majitel)

# def nebo function a nazev funkce ():

def greetUser ():
    print('Ahoj')
greetUser()

def greetUser (name):
    print('Ahoj', (name))
greetUser()

def sumTwoNumbers(a,b):
    return a + b
result = sumTwoNumbers(5,9)
print(result)
