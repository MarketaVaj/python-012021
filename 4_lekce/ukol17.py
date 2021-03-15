# Streamovací služba podruhé
# Pokračuj ve své práci pro streamovací službu. Služba nyní eviduje uživatele, kteří službu využívají. Vytvoř třídu Uzivatel, která bude mít atributy uzivatelske_jmeno a delka_sledovani, který udává celkovou délku pořadů, které uživatel zhlédl. Uživatelské jméno získej jako parametr a délka sledování je na začátku 0.
#
# Třídám Serial a Film přidej funkce get_celkova_delka(), která vrátí celkovou délku filmu/seriálu (u seriálu je to počet episod násobený délkou jedné episody).
#
# Třídě Uzivatel přidej funkci pripocti_zhlednuti(), která bude mít jeden parametr. Funkce zvýší atribut udávající celkovou délku sledávní o zadaný parametr.
#
# Vytvoř objekt, který reprezentuje nějakého uživatele. Následně zkus uvažovat situaci, že uživatel zhlédne film a seriál, které jsi vytvořil(a) jako objekty. Uživateli připočti délky děl k délce sledování, využij k tomu funkci get_celkova_delka() u objektu a seriálu, abys zjistil(a), kolik minut (nebo hodin) videa celkem uživatel zhlédl.
#
# Nejjednodušší řešení je, pokud si u filmu/seriálu uložíš celkovou délku do pomocné proměnné a tuto pomocnou proměnnou potom předáš jako parametr funkci pripocti_zhlednuti().
#
# Složitější varianta
# V pokročilejší variantě neeviduj pouze délku sledování ale i to, jaké pořady uživatel sledoval. Namísto délky sledování vytvoř atribut, který bude udávat zhlédnuté pořady (ideální pro tento účel je seznam). Dále přidej funkci zhledni_polozku(), která do seznamu zhlédnutých pořadů přidánovou položku.
#
# Dále vytvoř funkci delka_sledování() pro uživatele, která projde položky v seznamu a vrátí celkovou délku všech pořadů, které uživatel zhlédl.
#
# Vytvoř si ukázkové objekty a ověř, že vše funguje.

class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr
    def get_info(self):
        return f"Nazev je {self.nazev} a žánrem je {self.zanr}. "

class Film(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka
    def get_info(self):
        return super().get_info() + f"Delka filmu je {self.delka}."

class Serial(Polozka):
    def __init__(self,nazev, zanr,pocet_epizod, delka_epizody):
        super().__init__(nazev, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epizody
        self.delka_serial = []
    def get_info(self):
        return super().get_info() + f"Pocet epizod je {self.pocet_epizod} a delka jedne epizody je {self.delka_epizody}."
    def get_celkova_serial(self):
        self.delka_serial =  self.delka_epizody * self.pocet_epizod
        self.delka_serial.append(self.delka_serial)

class Uzivatel:
    def __init__(self, uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = [0]
    def get_info(self):
        return f"Uživatel/ka se jmenuje {self.uzivatelske_jmeno}"

    def assignPolozka(self, polozka):
        if polozka.delka:
            self.delka_sledovani.append(self.delka)
        if polozka.delka_epizody:
            self.delka_sledovani.append(self.delka_serial)

    def delkaSledovani (self):
        return (self.delka_sledovani)


prvniserial = Serial("Good doctor", "drama", 18, "40 minut")
prvnifilm = Film ("Krajina ve stinu", "drama", "3 hodiny")
print(prvnifilm.get_info())
print(prvniserial.get_info())

jana = Uzivatel("Jana")
print(jana.get_info())
print(jana.delkaSledovani())

# nepripocitava to a vypisuje porad nulu, ja vim