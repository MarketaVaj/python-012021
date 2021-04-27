# ¶Házení kostkami
# to dáš
# Mějme dvě hrací kostky, kterými vždy hodíme najednou a zaznamenáme součet bodů. Stáhněte si textový soubor kostky.txt, který obsahuje 1000 takových nezávislých hodů.
#
# Načtěte tato data do Python seznamu, ze kterého vyrobte sérii. Zobrazte histogram hodů. Zvolte vhodné rozložení přihrádek a zodpovězte následující dotazy:
#
# Jaká je nejčastější hodnota, která na dvou kostkách padne?
# Je větší šance, že padne hodnota 12 než že padne hodnota 2?

# import pandas
# kostky = pandas.read_csv('https://kodim.cz/czechitas/progr2-python/python-pro-data-1/vizualizace/excs/hazeni-kostkami/assets/kostky.txt', header=None)
#
# print(kostky.shape)
#
# kostky = kostky.iloc[:,0]
#
#
# kostky.hist(bins=[2,3,4,5,6,7,8,9,10,11,12,13])
#
# import matplotlib.pyplot as plt
# plt.show()

# 2
# ¶Call centrum
# V souboru callcentrum.txt najdete několik tisíc záznamů pro call centrum, které udávají časy mezi jednotlivými příchozími hovory v minutách a vteřinách. Načtěte tato data do série v Pythonu. Časy převeďte na vteřiny a zobrazte jejich histogram a boxplot. Co lze z těchto dvou grafů vyčíst?

import pandas
callCentrum = pandas.read_csv('https://kodim.cz/czechitas/progr2-python/python-pro-data-1/vizualizace/excs/call-centrum/assets/callcentrum.txt', header=None)

print(callCentrum.shape)

callCentrum = callCentrum.iloc[:,0]
casy = pandas.to_datetime(callCentrum, format="%M:%S")
print(callCentrum)

casy.hist(bins=15)
#
import matplotlib.pyplot as plt
plt.show()
#
# https://www.loom.com/share/8d60cacdeda740b88ff8f45657b18789?fbclid=IwAR3vV2cBtg8yukbHQaQE3mKZq0VCydl2OiAiNhN4zZ4po9cKBabKi_7rac8

