# Evidence aut
# Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 3 automobily:
#
# Registrační značka	Značka a typ vozidla	Počet najetých kilometrů
# 4A2 3020	Peugeot 403 Cabrio	47534
# 1P3 4747	Škoda Octavia	41253
# Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy:
#
# registrační značka automobilu,
# značka a typ vozidla,
# počet najetých kilometrů,
# informaci o tom, jestli je vozidlo aktuálně volné (pravdivostní hodnota -- True pokud je volné a False pokud je vypůjčené).
# Vytvoř funkci __init__ pro třídu Auto. Registrační značku, značku a typ vozidla a počet kilometrů získej jako parametry funkce __init__ a ulož je jako atributy objektu. Poslední atribut nastav jako False, tj. na začátku je vozidlo volné.
#
# Vytvoř objekty, které reprezentují všechny automobily půjčovny.

class Auto:
#    def get_info(self):
#       return f" Typ vozu {self.typvozu} s pozvanaci znackou {self.znacka} a poctem najetych kilometru {self.kilometry} je dostupny pokud True, nedostupny pokud False - {self.dostupnost}."
    def __init__(self, znacka, typvozu, kilometry, dostupnost=True):
        self.znacka = znacka
        self.typvozu = typvozu
        self.kilometry = kilometry
        self.dostupnost = dostupnost

peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio",47534, False )
skoda = Auto("1P3 4747", "Škoda Octavia",41253)

#print(peugeot.get_info())
#print(skoda.get_info())


