# import  wget
# wget.download("http://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")

import pandas
nakupy = pandas.read_csv('nakupy.csv')
# # print(nakupy)
# nakupy.info()
# print(nakupy.shape)
# print(nakupy.shape[0])
# print(nakupy.columns)
# print(nakupy.iloc[3]) vypise jenom nakup na pozici 4
print(nakupy.iloc[0:5]) zobrazi prvnich 5 radku
