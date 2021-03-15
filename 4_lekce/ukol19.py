# Instalace modulu
# Zopakuj si postup při instalaci modulu. Pojďme si vytvořit směnárnu, která nemá kurzy zadané pevně, ale umí si kurz měny stáhnout z internetu.
#
# V PyCharmu klikni na File -> Settings -> Project -> Python Interpreter. Následně klikni na tlačítko + (Install) a vyhledej modul forex-python. Dále klini na Install Package a potvrď instalaci.
#
# Dále se podívej na následující příklad, jak s modulem pracovat. Na prvním řádku je import, aby Python věděl, že s modulem chceme pracovat. Na druhém řádku vytvoříme objekt prevodnik (je to objekt třídy CurrencyRates), který se stará o převod měn.
#
# Uvažujme třeba, že chceme spočítat, kolik by nás stálo, pokud bychom chtěli 10 dolarů. Použijeme funkci convert(), která má jako první parametr zkraktu cílové měny, jako druhé parametr zkratku zdrojové měny a jako třetí parametr množství požadovaných dolarů. Funkce vypočte, kolik jednotek zdrojové měny je potřeba zaplatit, aby to odpovídalo požadovanému množství cílové měny.
#
# from forex_python.converter import CurrencyRates
# prevodnik = CurrencyRates()
# pozadovano_v_cilove_mene = 10
# cena_v_korunach = prevodnik.convert('USD', 'CZK', pozadovano_v_cilove_mene)
# print(cena_v_korunach)
# Zkus program upravit tak, aby zjistil požadovanou měnu od uživatele (pomocí funkce input()). Uvažuj, zkus např. pracovat s měnami EUR, GBP nebo DKK. Následně od uživatele získej i požadované množství cílové měny. Nezapomeň toho množství převést na typ int.
#
# Pokročilejší varianta
# Podívej se do dokumentace k modulu forex-python. Zjistíš, že umí pár dalších zajímavých věcí, například převod měny do Bitcoinu. Zkus pomocí modulu vytvořit program, který se zeptá uživatele na měnu a požadovaný počet Bitcoinů a vrátí mu množství měny, které by potřeboval, aby požadované množství Bitcoinů mohl koupit.

menauzivatele = input("Jaku menu potrebujes?")
pozadovano = int(input("Kolik jednotek pozadovane meny chces?"))

from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = pozadovano
cilovamena = menauzivatele
cena_v_korunach = prevodnik.convert(cilovamena, 'CZK', pozadovano_v_cilove_mene)
zaokrouhlenacena= round(cena_v_korunach)
print (zaokrouhlenacena)

yourCurrency = input ("Jakou menu mas?")
pozadovaneBitcoiny = int(input("Kolik jednotek Bitcouinu chces?"))

from forex_python.bitcoin import BtcConverter
b = BtcConverter() # force_decimal=True to get Decimal rates

cenaBitCelkem = b.get_latest_price(yourCurrency)*pozadovaneBitcoiny
zaokrouhlenaCenaBitCelkem = round(cenaBitCelkem)

cenaJedenBitcoin = b.get_latest_price(yourCurrency)

print("cena za 1 Bitcoin", (cenaJedenBitcoin))
print ("Zaokrouhlena cena za pozadovane Bitcoiny", (zaokrouhlenaCenaBitCelkem), ".")