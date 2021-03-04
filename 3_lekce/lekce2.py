# class Employee:
#     def take_holiday (self, days):
# #        self.holidays -= days
#         if self.holidays >= days:
#             self.holidays = self.holidays - days
#             return  "Dovolena schvalena."
#         else:
#             return "Muzes si vzit pouze"
#
#
# frantisek.take_holiday(80)
#
#
# ¶ Kniha
# Zkus pro našeho nakladatele vytvořit software s využitím tříd a objektů. Vytvoř tedy třídu Book, která reprezentuje knihu. Každá kniha bude mít atributy title, pages a price. Hodnoty nastav ve funkci __init__.
#
# Přidej knize funkci getInfo, která vypíše informace o knize v nějakém pěkném formátu.
# Občas se stane, že se kniha moc neprodává a knihkupec se snaží nalákat kupující slevou. Přidej funkci discount, která bude mít jeden parametr - velikost slevy v procentech. Funkce sníží cenu knihy o dané procento.

class Book:
    def get_info(self):
        return (f"Zajimava kniha {self.title}, s poctem stranek {self.pages}, s cenou {self.price} Kc, po sleve {self.price - self.discount * self.price} Kc.")

    def __init__(self, title, pages, price, discount = False):
        self.title = title
        self.pages = pages
        self.price = price
        self.discount = discount

kniha1 = Book("Kridak",123, 34, 0.01)

print(kniha1.get_info())
