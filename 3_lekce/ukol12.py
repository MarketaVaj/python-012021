# Půjčení auta
# Pokračuj ve své práci pro autopůjčovnu, kterou jsi začala v příkladu 11.
#
# Třídě Auto přidej funkci pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr. Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, vrátí text "Potvrzuji zapůjčení vozidla" a změní hodnotu atributu, který určuje, zda je vozidlo půjčené. Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici".
#
# Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.
#
# Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto.
#
# Dotaz na uživatele a výpis výsledků si v programu zkopíruj, abys dokázala otestovat, že funkce nedovolí půjčit stejné auto dvakrát.

class Auto:
    def get_info(self):
        return f" Typ vozu {self.typvozu}s pozvanaci znackou {self.znacka} a poctem najetych kilometru {self.kilometry} je dostupny pokud True, nedostupny pokud False - {self.dostupnost}."
    def __init__(self, znacka, typvozu, kilometry, dostupnost=True):
        self.znacka = znacka
        self.typvozu = typvozu
        self.kilometry = kilometry
        self.dostupnost = dostupnost

peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio",47534, False )
skoda = Auto("1P3 4747", "Škoda Octavia",41253)

print ('Auta v nabidce:')
print(peugeot.get_info())
print(skoda.get_info())

class Auto:
    def pujc_auto(self):
        self.dostupnost = dostupnost
        if self.dostupnost == True:
            self.dostupnost = False
            dostupnost = 'Potvrzuji zapůjčení vozidla.'
        else:
            dostupnost = 'Vozidlo není k dispozici.'
            return dostupnost

vozidlo = input('Jakou znacku vozidla si chces pujcit? Muzes si vybrat Peugeot nebo Skodu.')
if vozidlo == 'Peugeot':
    print(peugeot.get_info())
    dostupnost = pujc_auto(self)
    print(dostupnost)
elif vozidlo == 'Skoda':
    print(skoda.get_info())
    dostupnost = pujc_auto(self)
    print(dostupnost)
else:
    print('Spatna znacka vozidla.')



