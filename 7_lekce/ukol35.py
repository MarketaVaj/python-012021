# Teplota ve městech popáté
# Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.
#
import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

# Vytvoř tabulku, která bude obsahovat údaje o teplotě za města Helsinki, Miami Beach a Tokyo.
# Vytvoř krabicový graf a porovnej rozsah teplot v těchto městech.

import pandas
teploty = pandas.read_csv("temperature.csv")
import pytemperature
import matplotlib.pyplot as plt

print(teploty)

vybraneStaty = teploty[(teploty["City"] == "Miami Beach") | (teploty["City"] == "Helsinki") | (teploty["City"] == "Tokyo")]

vybraneStaty = vybraneStaty[["City", "AvgTemperature"]]

ax = vybraneStaty.boxplot(by="City", whis=[0, 100])
ax.set_ylabel("Teploty")
ax.set_xlabel("Město")
ax.set_title("Porovnani teplot")
plt.show()