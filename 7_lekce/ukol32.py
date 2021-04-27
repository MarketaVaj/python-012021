# Histogram platů
# Stáhni si znovu soubor platy_2021_02.csv s informacemi o platech v softwarové firmě, se kterými jsme již pracovali v příkladu 26.
#
# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")
# #
# Načti si tato data do tabulky a vytvoř histogram. Nastav vhodně hranice skupin histogramu (parametr bins), aby byl graf přehledný a snadno interpretovatelný.

import pandas
platy = pandas.read_csv('platy_2021_02.csv')
print(platy)

jenomPlaty = platy.iloc[:,1]
# print(jenomPalty)
#
import matplotlib.pyplot as plt
jenomPlaty.hist(bins=[30000, 32000, 34000, 36000, 38000, 40000, 42000,44000, 46000, 48000, 50000, 52000, 54000, 56000, 58000, 60000])
plt.show()


# Dobrovolný doplněk
# Vyzkoušej si vytvořit podgrafy. pandas a matplotlib to umí poměrně jednoduše a to pomocí parametru by metody hist(). Jako parametr vlož sloupec, podle kterého chceš data do podgrafů rozdělit. Musíš vložit sloupec ve formě dat, nikoli pouze jeho název.
#
# Vytvoř pro zadaná data podgrafy pro jednotlivá města. Načti si informace o městě, ve kterém jednotliví pracovníci pracují (to jsme již dělali v příkladu) příkladu 26. Následně sloupec mesto použij na rozdělení podgrafů.
#
# Příklad výstupu je na obrázku níže.

