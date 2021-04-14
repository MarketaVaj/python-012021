# ¶Studenti
# zapni hlavu
# Stáhněte si datové sety, se kterými budeme pracovat v tomto cvičení: jmena100.csv, studenti1.csv, studenti2.csv. První set už známe z minulé lekce. Druhé dva sety obsahují seznam studentů na nějaké menší IT fakultě. Proveďte následující úkoly a zodpovězte předložené otázky.
#
# Načtěte dva datové sety studentů do oddělených pandas DataFrame a pomocí funkce concat je spojte do jednoho setu.
# Pokud studentovi chybí ročník, znamená to, že již nestuduje. Pokud mu chybí číslo skupiny, znamená to, že jde o dálkového studenta. Kolik studentů v datovém setu již nestuduje a kolik jsou dálkoví studenti?
# Vyčistěte data od studentů, kteří nestudují nebo studují jen dálkově. Nadále budeme pracovat pouze s prezenčními studenty.
# Zjistěte, kolik prezenčních studentů je v každém z oborů.
# Zjistěte průměrný prospěch studentů v každém oboru.
# Načtěte datový set s křestními jmény. Proveďte join s tabulkou studentů tak, abychom věděli pohlaví jednotlivých studentů.
# Zjistěte, zda na naší fakultě studují IT spíše ženy nebo spíše muži.

# import wget
# wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/jmena.csv')
# wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/studenti1.csv')
# wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/studenti2.csv')

import pandas
studenti1 = pandas.read_csv('studenti1.csv')
stupdenti2 = pandas.read_csv('studenti2.csv')
#

#!1
studenti_celkem = pandas.concat([studenti1, stupdenti2], ignore_index=True)
# print(studenti_celkem)

#2
# print(studenti_celkem["ročník"].isnull())
# print(studenti_celkem["ročník"].isnull().shape)
# print(studenti_celkem[studenti_celkem["ročník"].isnull()].shape)
#
# print(studenti_celkem.columns)
# print(studenti_celkem[studenti_celkem['kruh'].isnull()].shape)

#3
# studenti_celkem =studenti_celkem.dropna()
# print(studenti_celkem)

#4
# studenti_celkem=studenti_celkem.dropna()
# print(studenti_celkem.shape)
# print(studenti_celkem.groupby('obor').count())

#5

# studenti_celkem=studenti_celkem.dropna()
# print(studenti_celkem.shape)
# print(studenti_celkem.groupby('obor').count())
#
# print(studenti_celkem.groupby("obor")["prospěch"].mean())

#6
jmena = pandas.read_csv('jmena.csv')
pandas.merge (studenti_celkem, jmena, on=['jméno'])
studenti_celkem.shape
studentiPlusJmena = pandas.merge(studenti_celkem, jmena)
print(studentiPlusJmena)

#7
print(studentiPlusJmena.groupby("pohlaví").count())

