# Hra o trůny
# Stáhni si soubor character-deaths.csv, která obsahuje informace o smrti některých postav z prvních pěti knih románové série Píseň ohně a ledu (A Song of Fire and Ice).
#
# Stažení souboru pomocí wget:
#
# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")

import pandas
# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")

postava

# Načti soubor do tabulky (DataFrame) a nastav sloupec Name jako index.
postava = postava.set_index("Name")

# Zobraz si sloupce, které tabulka má. Posledních pět sloupců tvoří zkratky názvů knih a informace o tom, jestli se v knize postava vyskytuje.

print(postava.loc[[],:])
print(postava.iloc[[],-5:])

# Použij funkci loc ke zjištění informací o smrti postavy jménem "Hali".

print(postava.loc[['Hali'],['Death Year']])

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam".

print(postava.loc["Gevin Harlaw":"Gillam"])

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a sloupce Death Year.

print(postava.loc["Gevin Harlaw":"Gillam",'Death Year'])

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a informace o tom, v jakých knihách se postava vyskytuje, tj. vypiš všechny sloupce mezi GoT a DwD.

print(postava.loc["Gevin Harlaw":"Gillam",'GoT':'DwD'])