# Teplota ve městech potřetí
# Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.
#
# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
teplota = pandas.read_csv("temperature.csv")
# print(teplota.head())
print(teplota.info())

# Pokud jsi v minulé lekci zpracovala rozšířené zadání, můžeš pracovat s teplotami ve stupních Celsia.
# Vyfiltruj si informace o teplotách 13. listopadu 2017.

mereniTrinacteho = teplota[teplota['Day'] == 13]
print(mereniTrinacteho)

# Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.

# minMereniTrinacteho=min(mereniTrinacteho['AvgTemperature'])
# print(minMereniTrinacteho)

mereniTrinacteho = teplota[(teplota['Day'] == 13) & (teplota['AvgTemperature'] > -99)]
print(mereniTrinacteho)

# Vypočti počet dat, které máš pro daný den za jednotlivé regiony.

print(mereniTrinacteho.groupby("Region")["Country"].count())

# Vypočti průměrnou teplotu za jednotlivé regiony.

print(mereniTrinacteho.groupby("Region")["AvgTemperature"].mean())

# Vypočti maximální a minimální teplotu v každém regionu.

print(mereniTrinacteho.groupby("Region")["AvgTemperature"].min())
print(mereniTrinacteho.groupby("Region")["AvgTemperature"].max())