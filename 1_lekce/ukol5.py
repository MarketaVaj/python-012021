# Detektivky podruhé
# Vraťme se k software pro našeho nakladatele. Nakladatel má nyní v software dva slovníky, které obsahují informace o prodejích knih v letech 2019 a 2020.
#
# Uvažuj, že uživatel se zajímá o prodeje konkrétní knihy. Zeptej se uživatele na název knihy a poté vypiš informaci o tom, kolik se této knihy celkem prodalo. Nezapomeň na to, že některé knihy byly prodávány pouze v jednom roce.

prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}
mojekniha = input('Zadej nazev knihy:')
prodejcelkem = 0
for mojekniha in prodeje2019:
    prodejcelkem [mojekniha] = prodeje2019[mojekniha]
    for mojekniha in prodeje2020:
        prodejcelkem [mojekniha] = prodejcelkem + prodeje2020[mojekniha]

print('Bylo prodano ', (prodejcelkem), '.')

