# import pandas
# # import wget
# # wget.download("https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/zakladni-dotazy/excs/ceska-jmena/assets/jmena.csv")
#
# jmena = pandas.read_csv("jmena.csv")
# jmena = jmena.set_index("jméno")
# #
# print(jmena.info())

# Vypište na konzoli informace o jménu Jiří.

# print(jmena.loc['Jiří'])  - series
# print(jmena.loc[['Jiří']]) - data frame

# Vypište na konzoli informace pro jména Martin, Zuzana a Josef.

#print(jmena.loc[['Martin', 'Zuzana', 'Josef']])

# Vypište na konzoli informace o všech nejčastějších jménech až po Jiřího.

# cetnaJmena = jmena["jméno"] == [:"Hana"])]
#print(jmena.loc[:"Hana"])

# SERAZENI: - seradi od nejvetsiho po nejmensi
#jmena = jmena.sort_values(by= 'četnost', ascending=False)
#print(jmena)

# Vypište pouze průměrné věky osob mající jména mezi Martinem a Terezou.
#print(jmena.loc['Martin':'Tereza', 'věk'])

# Vypište průměrný věk a původ pro všechna jména od Libora dolů.
# print(jmena.loc['Libor': , ['věk', 'původ']])

# Vypište sloupečky mezi věkem a původem pro všechna jména v tabulce.
#print(jmena.loc[:, 'věk':'původ'])  #- vypise vcerne veku a puvodu
# print(jmena.iloc[:, 2:-1]) -  vypise jake radsi jsou mezi

import pandas
# import wget
# wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/excs/ceska-jmena-2/assets/jmena.csv")

jmena = pandas.read_csv("jmena.csv")
jmena = jmena.set_index("jméno")


greated_60 = jmena['věk'] > 60
print(greated_60)

#print(jmena.info())

# podminka = (jmena['původ'] == 'hebrejský') | (jmena['původ'] == 'slovanský')
# # podminka = (jmena['původ'].isin(['hebrejský','slovanský'])
# print(jmena[podminka])


