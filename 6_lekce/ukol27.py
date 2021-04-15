# Projekty
# import wget
# #
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

# Pokračuj ve své práci pro softwarovou firmu. Ze souboru vykazy.csv načti informace o výkazech na projekty pro jednoho vybraného zákazníka.
# Načti data ze souboru a ulož je do tabulky.

import pandas
vykazy = pandas.read_csv("vykazy.csv")
# print(vykazy)

# Proveď agregaci a zjisti celkový počet vykázaných hodin za jednotlivé projekty.

print(vykazy.groupby("project")["hours"].sum())

# Dobrovolný doplněk
# Propoj tabulku s výkazy s tabulkou se zaměstnanci, kterou jsi vytvořil(a) v předchozím cvičení. Následně proveď statistiku vykázaných hodin za jednotlivé kanceláře, tj. spočítej celkový počet hodin vykázaný zaměstnanci jednotlivých kanceláří na projekty daného zákazníka.

zamestnanci = pandas.read_csv("zamestnanci.csv")
# print(vykazy)

vykazy = vykazy.rename(columns={"emloyee_id": "cislo_zamestnance"})
# print(vykazy.shape)

zamestnanciProjekty = pandas.merge(zamestnanci, vykazy)
print(zamestnanciProjekty)

print(zamestnanciProjekty.groupby("mesto")["hours"].sum())

print(zamestnanciProjekty.groupby(["mesto", "project"])["hours"].sum())

# print(zamestnanciProjekty.shape)

# UKOL 30
zamestnanciProjekty.to_excel("zamestanciProjekty.xlsx")