
# import wget
#
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

import pandas
plzen = pandas.read_csv("zam_plzeň.csv ")
liberec = pandas.read_csv("zam_liberec.csv")
praha = pandas.read_csv("zam_praha.csv")

# Načti data o zaměstnancích z CSV souborů do tabulek (DataFrame). Ke každé tabulce přidej nový sloupec mesto, které bude obsahovat informaci o tom, ve kterém městě zaměstnanec pracuje.

plzen["mesto"] = "plzen"
liberec["mesto"] = "liberec"
praha["mesto"] = "praha"

# print(praha)

# Vytvoř novou tabulku zamestnanci a ulož do ní informace o všech zaměstnancích.

zamestnanci = pandas.concat([plzen, liberec, praha])
# print(zamestnanci)
zamestnanci.to_csv("zamestnanci.csv", index=False)

# Ze souboru platy_2021_02.csv načti platy zaměstnanců za únor 2021. Propoj tabulku (operace join) s platy a tabulku se zaměstnanci pomocí sloupce cislo_zamestnance.

platy = pandas.read_csv("platy_2021_02.csv")

zamestanciSPlaty = pandas.merge(zamestnanci, platy, on="cislo_zamestnance")
# print(zamestanciSPlaty)

# Porovnej rozměry tabulek před spojením a po spojení. Pokud nemá některý zaměstnanec plat za únor, znamená to, že v naší firmě již nepracuje.
# print(platy.shape)
# # print(platy.info)
print(zamestnanci.shape)
print(zamestanciSPlaty.shape)

# Spočti průměrný plat zaměstnanců v jednotlivých kancelářích.

# print(zamestanciSPlaty.groupby("mesto")["plat"].mean())

# Dobrovolný doplněk
# Ulož do proměnné počet zaměstnaců, kteří v naší firmě již nepracují.

spojenitabulek = pandas.merge(zamestnanci, platy, how="outer")
print(spojenitabulek)
uznepracuji = spojenitabulek['plat'].isnull()
print(uznepracuji)


# V rámci úspory se IT oddělení rozhodlo prověřit licence přidělené zaměstnancům, kteří ve firmě již nepracují. Vytvoř samostatnou tabulku, která obsahuje jména zaměstnanců, kteří ve firmě již nepracují. Tabulku ulož do souboru CSV.

# vim ze tu chybi jmena

uznepracuji.to_csv("uznepracuji.csv", index=False)
