# Teplota ve městech
# Stáhni si soubor temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.
#
# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
# Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky.
#
# Dále napiš následující dotazy:
#
# Pokročilá varianta
#
# Nainstaluj si modul pytemperature a zkus si vytvořit nový sloupec, který bude obsahovat průměrnou templotu ve stupních Celsia. Ve svém programu nejprve proveď import modulu pytemperature. Nový sloupec pak přidáš do tabulky tak, že nalevo od = vložíš tabulku a název nového sloupce do hranatých závorek. Napravo pak můžeš provádět výpočty pomocí již existujících sloupců. Můžeš např. použít funkci f2c z modulu pytemperature, která převede teplotu ze stupňů Fahrenheita na stupně Celsia.
#
# import pytemperature
# df["AvgTemperatureCelsia"] = pytemperature.f2c(df["AvgTemperature"])
# Nyní můžeš zpracovat následující příklady:


import pandas
# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

teplota = pandas.read_csv('temperature.csv')

# print(teplota.head())


# Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního? Napadá tě, čím to může být? Zde je nápověda.

teplota = teplota.set_index("City")
print(teplota.loc[["Prague"]])

# Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.

mereni = teplota[teplota['AvgTemperature'] > 80]
print(mereni)

# Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).

mereni = teplota[(teplota['AvgTemperature'] > 60) & (teplota['Region'] == 'Europe')]
print(mereni)

# Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.

mereni = teplota[(teplota['AvgTemperature'] > 80) | (teplota['AvgTemperature'] < -20)]
print(mereni)

import pytemperature
teplota["AvgTemperatureCelsia"] = pytemperature.f2c(teplota["AvgTemperature"])

print(teplota)

#
# Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 30 stupňů Celsia.

teplota=teplota.set_index("Country")
mereni = teplota[(teplota['AvgTemperatureCelsia'] > 30)]
print(mereni)

# Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).

mereni = teplota[(teplota['AvgTemperatureCelsia'] > 15) & (teplota['Region'] == 'Europe')]
print(mereni)

# Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo menší než -10 stupňů. Jsou některé hodnoty podezřelé?

mereni = teplota[(teplota['AvgTemperatureCelsia'] > 30) | (teplota['AvgTemperatureCelsia'] < -10)]
print(mereni) #jo Afrika -72 stupnu
