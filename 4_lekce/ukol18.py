# Inverview
# Uvažuj následující třídu Kontakt, která slouží k evidenci všech kontaktů (např. zákazníků, zaměstnanců, uchazečů o práci atd.).
#
# class Kontakt:
#   def __init__(self, jmeno, email):
#     self.jmeno = jmeno
#     self.email = email
# Vytvoř třídu Uchazec, která bude dědit od třídy Kontakt a která reprezentuje uchazeče o práci. Uchazeč o práci bude mít navíc atribut datum_pohovoru a zapis_z_pohovoru. Datum pohovoru objekt získá z parametru a zápis z pohovoru je na začátku prázdný řetězec "".
#
# Dále přidej funkci uloz_zapis(), která bude mít jako parametr textový zápis pohovoru. Tato funkce ohlídá, zda uživatel omylem nezadává zápis k pohovoru, který ještě neproběhl. Na začátku funkce porovnej aktuální datum a datum pohovoru. Pokud podle data pohovor ještě neproběhl, vrať chybový text, který informuje uživatele o chybě. Pokud již podle data pohovor proběhl, ulož zápis a vrať text s informací, že zápis byl uložen.

class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email

class Uchazec(Kontakt):
    def __init__(self, jmeno, email, datum_pohovoru, zapis_z_pohovoru):
        super().__init__(jmeno, email)
        self.datum_pohovoru = datum_pohovoru
        self.zapis_z_pohovoru = ""
    def get_info(self):
        return F"{self.jmeno} , {self.email} , {self.datum_pohovoru}, {self.zapis_z_pohovoru}"

    # def uloz_zapis(self):
    #     if self.datum_pohovoru <= dnesni datum????
    #         self.zapis_z_pohovoru = ????
    #         return f"Zapis bylo ulozen"
    #     else:
    #         return f"Pohovor jeste neprobehl."


jana = Uchazec("Jana", "mmmm", "2.3.2021", "ahoj")
print(jana.get_info())