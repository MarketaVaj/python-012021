# Vakcíny
# Stáhni si soubor country_vaccinations.csv o průběhu očkování proti nemoci COVID-19.
#
# Stažení souboru pomocí wget:
#
# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")
# Dále napiš následující dotazy:
#

import pandas

# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")

vakcina = pandas.read_csv('country_vaccinations.csv')
# print(vakcina)

# Dotaz na počty očkovaných (sloupec total_vaccinations) v jednotlivých státech dne 2021-03-10 (s datem pracuj úplně stejně jako s řetězcem, tj. nevyužívej modeul datetime, ale vlož do dotazu přímo řetězec).
#
vakcina = vakcina.set_index("date")
pocet = vakcina.loc[["2021-03-10"], ["total_vaccinations"]]
print(pocet.sum())

# Dotaz na řádky, kde 2021-03-10 bylo naočkováno více než 1 mil. obyvatel.

ockovani_nad_milion= vakcina [(vakcina["date"] == '2021-03-10') & (vakcina["daily_vaccinations"] > 1_000_000 )]
print (ockovani_nad_milion)

# Podíváme se na extrémní hodnoty. Napiš dotaz na řádky, kde za daný den naočkování více než 100 tisíc lidí nebo naopak méně než 100 lidí.

ockovani_extrem = vakcina [(vakcina["daily_vaccinations"] < 100) | (vakcina["daily_vaccinations"] > 1_000_000 )]
print (ockovani_extrem)

# Dobrovolný doplněk
#
# Vypiš informace o očkování za dny 2021-03-10 a 2021-03-11 pro státy United Kingdom, Finland a Italy. Použij např. funkci isin().
ukol = vakcina[(vakcina ['date'].isin(['2021-03-10','2021-03-11'])) & (vakcina ['country'].isin(['United Kingdom', 'Finland','Italy']))]
print(ukol)

# Vypiš informace o očkování pro Japan mezi daty 2021-03-03 a 2021-03-09. Data v tomto formátu můžeš porovnávat pomocí operátorů >= a <= jako řetězce, tj. opět nemusíš použít modul datetime.

druhyUkol = vakcina[(vakcina ['date'] > '2021-03-03') & (vakcina ['date'] < '2021-03-09') & (vakcina["country"] == 'Japan')]
print(druhyUkol)
