# import  wget
# wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/excs/nabidky/assets/DataAnalyst.csv")

import pandas
jobs = pandas.read_csv('DataAnalyst.csv', index_col=0)

# vypis sloupecky
#print(jobs.columns)
#
# # vypis pocet radku a sloupecku
#print(jobs.info())
#print (jobs.shape)
#
# # informace o pozici na 10 radku
#print(jobs.loc[9])
#print(jobs.loc[9] ['Job Description'])

# kde budou pracovat zajemci na 12-20 radku
print(jobs.iloc[11:21], ['Job Title'])