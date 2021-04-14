# import wget
# soubory =['https://kodim.cz/czechitas/python-data/datova-analyza/pandas-agregace/assets/u202.csv', 'https://kodim.cz/czechitas/python-data/datova-analyza/pandas-agregace/assets/u203.csv', 'https://kodim.cz/czechitas/python-data/datova-analyza/pandas-agregace/assets/u302.csv']
#
# for soubory in soubory:
#     wget.download(soubory)

#
import pandas
u202 = pandas.read_csv('u202.csv').dropna()
u203 = pandas.read_csv('u203.csv').dropna()
u302 = pandas.read_csv('u302.csv').dropna()
u202["místnost"] = "u202"
u203["místnost"] = "u203"
u302["místnost"] = "u302"
# # print(u202.head()) / vypise hlavicku
# # print(u202[u202['známka'].isnull()])
#
maturita = pandas.concat([u202, u203, u302], ignore_index=True)
# # print(maturita)
#
maturita.to_csv("maturita.csv", index=False)

# import wget
# wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/studenti.csv")

studenti = pandas.read_csv('studenti.csv')
vysledky_se_jmeny = pandas.merge(maturita, studenti)
print(vysledky_se_jmeny.head())

vysledky_se_jmeny_a_predsedajici = pandas.merge(vysledky_se_jmeny, predsedajici)

vysledky_se_jmeny_a_predsedajici = pandas.merge(u202,studenti, how="left")


nakupy = pandas.read_csv('nakupy.csv')
print(nakupy.groupby("Jméno").sum())