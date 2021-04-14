import pandas
# import  wget
# wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/assets/staty.json")
#
staty = pandas.read_json("staty.json")
staty = staty.set_index("name")
#
#print(staty.info())
#print(staty.index)
#
# print (staty.loc["Czech Republic"]) #loc bude vypisovat radky ktere jsme si pojmenovali v set_index name
#
#print (staty.loc["Czech Republic":"Dominican Republic"]) #vypise vsechno od CZ po Dom, vcetne, to je jinak nez u ILOC, ktery posledni cislo nebere v potaz
#
#print (staty.loc["Czech Republic":])#od ceksa dal
# print (staty.loc[["Slovakia", "Austria", "Poland"], ["gini", "population"]]) #vybere zeme a sloupecky co ma vybrat

# populace = staty["population"]
# print(populace.sum())
#
# pidistaty = staty[staty["population"] < 1000]
# print(pidistaty[["area", "population"]])


lidnate_evropske_staty = staty [(staty["population"] > 20000000) & (staty["region"] == "Europe")]
print (lidnate_evropske_staty)




