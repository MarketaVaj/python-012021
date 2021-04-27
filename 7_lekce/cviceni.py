# import wget
# wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/assets/staty.json")

# import pandas
# staty = pandas.read_json('staty.json')
# staty = staty.set_index("name")
#
# staty['population_destiny'] = staty["population"]/staty['area']
# staty = staty.sort_values(['population_destiny','area'], ascending=(False, True))
# print(staty.head())

import matplotlib.pyplot as plt
import pandas
import datetime as dt

# pocatecni_zustatek = 10000
pohyby = [746, 52, -749, -63, 71, 958, 157, -1223, -1509, -285, -350, 728, -260, 809, -164, 243, -238, 233, -646, -82, -275, 179, 417, 149, 301, 957, -711, 376, 421, -15, -663]
# pohyby[0] += pocatecni_zustatek

datumy = []
for d in range(1, 32):
  novy_datum = dt.date(2019, 3, d)
  datumy.append(novy_datum)
  #datumy = datumy + [novy_datum, ]
print(datumy)

pohyby_na_uctu = pandas.Series(pohyby, index=datumy)
fig = pohyby_na_uctu.plot(kind="bar", color= "red", grid=True)
fig.set_ylabel('Zůstatek v korunách')
fig.set_xlabel('Datum')
plt.ylim(-2000, 2000)
plt.show()

# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
# popis sloupecku

muzi = pandas.Series([
  179.3, 183.7, 181.4, 176.0, 183.6, 184.7, 163.4, 180.3,
  167.5, 166.8, 173.5, 172.5, 173.0, 177.6, 176.0, 179.5,
  182.6, 172.0, 183.2, 177.0, 176.2, 175.7, 174.3, 180.3,
  184.9, 171.1, 182.3, 169.7, 181.3, 188.8, 176.8, 159.0,
  180.3, 198.5, 185.8, 191.0, 170.9, 196.0, 183.3, 183.0,
  189.9, 184.8, 184.0, 183.1, 184.0, 190.7, 191.7, 187.8,
  177.5, 177.5, 189.2, 188.4, 195.0, 204.2, 180.2, 181.3,
  178.2, 182.6, 172.1, 175.7, 180.7, 181.2, 165.0, 188.6
])

zeny = pandas.Series([
  172.0, 169.0, 166.8, 164.6, 172.7, 171.5, 167.0, 167.0,
  168.3, 184.7, 166.0, 160.0, 168.8, 165.8, 173.5, 163.0,
  168.9, 158.4, 166.4, 169.4, 174.2, 175.6, 167.2, 168.0,
  171.5, 168.8, 168.9, 174.1, 169.0, 170.7, 156.3, 174.8,
  169.1, 161.4, 172.5, 166.1, 171.5, 163.9, 164.5, 169.0,
  168.5, 163.3, 169.5, 167.4, 175.5, 165.0, 166.6, 158.9,
  164.5, 168.7, 161.6, 175.8, 179.0, 167.9, 161.1, 167.6,
  165.9, 165.2, 176.0, 179.4, 160.1, 163.8, 177.7, 160.4
])

vysky = muzi.to_frame(name='muži')
vysky['ženy'] = zeny
vysky.plot(kind='box', whis=[10,90])
# muzi.plot(kind='box', whis=[10,90])
plt.show()

