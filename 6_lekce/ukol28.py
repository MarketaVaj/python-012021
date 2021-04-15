# Státy světa potřetí
# import wget
# #
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")
# V souboru staty.json jsou uložena data s informacemi o státech světa, se kterými jsme již pracovali. Zkusme nyní zpracovat podobné úlohy pomocí pandas.
#
# Načti data ze souboru do tabulky.

import pandas
staty =pandas.read_json('staty.json')
print(staty.info())
# Vyfiltruj státy, které leží v Evropě.

evropa = staty[(staty["region"]=="Europe")]
print(evropa)
print(staty[(staty["region"]=="Europe")])

# Zjisti počet států v jednotlivých subregionech Evropy.

print(evropa.groupby("subregion")["name"].size())

# Zjisti cekový počet obyvatel v jednotlivých subregionech Evropy.

print(evropa.groupby("subregion")["population"].sum())

# Rozšíření zadání
# V souboru staty.json jsou uložena data s informacemi o státech světa, se kterými jsme již pracovali. V souboru gdp.csv jsou dále informace o hrubém domácím produktu (Gross Domestic Product - GDP) států za roky 2017-2019 ze Světové banky.
#
# Načti informace ze souborů do tabulek. Z tabulky s GDP odeber státy, které nemají kompletní informace GDP (tj. ponech pouze státy, které mají kompletní data za všechny tři roky).

gdp =pandas.read_csv('gdp.csv').dropna()
print(gdp)

# Propoj obě tabulky podle třípísmenného kódu států.

staty = staty.rename(columns={"alpha3Code": "Country Code"})
# print(staty.info())
statyGdp = pandas.merge (staty,gdp, on='Country Code')
print(statyGdp.info())

# Spočti celkové HDP za rok 2019 a celkový počet obyvatel za jednotlivé subregiony.

GdpZaRok = (statyGdp.groupby('subregion')["population","2019"].sum())
print(GdpZaRok)

# Projdi si subkapitolu o počítaných sloupcích (část o podmínených sloupcích není nutné číst). K tabulce, kterou jsi vytovřila v předchozím kroku, vypočti GDP v roce 2019 na obyvatele, tj. přidej sloupec s velikostí GDP v roce 2019 vydělenou počtem obyvatel daného subregionu.

GdpZaRok["GdpNaObyvatele"] = GdpZaRok["2019"] / GdpZaRok["population"]
print(GdpZaRok)


