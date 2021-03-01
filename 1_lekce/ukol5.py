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
#    "Zkus mě chytit": 6671,
}
prodejcelkem = 0
mojekniha = input('Zadej nazev knihy:')
if mojekniha in prodeje2019:
    prodejcelkem += prodeje2019[mojekniha]
    if mojekniha in prodeje2020:
        prodejcelkem += prodeje2020[mojekniha]
        print('Bylo prodano ', (prodejcelkem), '.')
else:
    print('Zadana kniha neni v nasem seznamu.')

#opravene od Jirky:
# Tady pozor na vnořenou podmínku. Jsou tam knížky, které jsou jen ve slovníku prodeje2020, ale nejsou ve slovníku prodeje2019. Pokud máš ale druhou podmínku vnořenou do první, tak pro tyto knížky program fungovat nebude. Můžeš mít třeba podmínky samostatně a následně vypsat text o tom, že knížka není na seznamu, pokud má nulové prodeje.

prodejcelkem = 0
mojekniha = input('Zadej nazev knihy:')
if mojekniha in prodeje2019:
    prodejcelkem += prodeje2019[mojekniha]
if mojekniha in prodeje2020:
    prodejcelkem += prodeje2020[mojekniha]

if prodejcelkem > 0:
    print('Bylo prodano ', (prodejcelkem), '.')
else:
    print('Zadana kniha neni v nasem seznamu.')