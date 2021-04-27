# Velikonoce
# Ze souboru velikonoce.csv načti data o tom, kolikrát na který datum připadaly Velikonoce v letech 1600 až 2100.

# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")

import pandas
velikonoce = pandas.read_csv('velikonoce.csv')
print(velikonoce)

# Vytvoř sloupcový graf, který data přehledně zobrazí. Na ose x budou vidět jednotlivá data ("datumy") a výška sloupce označí, kolikrát na daný den připadly Velikonoce.

import matplotlib.pyplot as plt


graf = velikonoce.plot(kind="bar")
graf.set_ylabel('Kolikrát byly Velikoncoe v tomto datu')
graf.set_xlabel('Datum')
graf.set_title("Kolikrat byli kdy Velikonoce")
plt.show()

# Tentokrát jsou popisky a titulek povinné :-)
#
# Po zavolání funkce plot() si výsledek ulož do proměnné ax. Následně zavolej metodu set_ylabel(), abys nastavila popisek osy y grafu.
#
# ax = velikonoce.plot()
# ax.set_ylabel("Počet dnů")