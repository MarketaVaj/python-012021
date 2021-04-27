# Řazení
# Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.
#
# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
# # Pokud jsi v předminulé lekci zpracovala rozšířené zadání, můžeš pracovat s teplotami ve stupních Celsia.
#
import pandas
teplota = pandas.read_csv("temperature.csv")
# print(teplota)

# Vyfiltruj si informace o teplotách 13. listopadu 2017.

mereniTrinacteho = teplota[teplota['Day'] == 13]
# print(mereniTrinacteho)

# Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.

mereniTrinacteho = teplota[(teplota['Day'] == 13) & (teplota['AvgTemperature'] > -99)]
# print(mereniTrinacteho)

# Seřad hodnoty v souboru podle teploty od největší po nejmenší.

# print(teplota.info())
serazeni = mereniTrinacteho.sort_values('AvgTemperature', ascending=False)
print(serazeni)

# Vypiš pět měst s nejvyšší teplotou a pět měst s nejnižší teplotou.

print(serazeni.head())
print(serazeni.iloc[:5])