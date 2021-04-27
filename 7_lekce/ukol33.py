# Twilio podruhé
# Stáhni si soubor twlo.csv, který obsahuje informace o vývoji ceny akcie firmy Twilio od začátku roku 2020. Soubor obsahuje informace o otevírací, minimální, maximální a uzavírací ceně za každý den.
#
# Stažení souboru pomocí wget:
#
# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")
# #
import pandas
import matplotlib.pyplot as plt
#
twilio = pandas.read_csv("twlo.csv")
print(twilio.info())
print(twilio)

# Výše uvedeným programem načti data o vývoji ceny akcie. Vytvoř čárový graf vývoje zavírací ceny akcie (sloupec Close) v čase.

twilio.plot("Date", "Close")
plt.show()

# Zkus nyní převést sloupec Date na typ datetime příkazem níže a vytvoř stejný graf jako předtím. Porovnej grafy a zjisti, co se změnilo.

twilio["Date"] = pandas.to_datetime(twilio["Date"])
twilio.plot("Date", "Close")
plt.show()

# osa x se zmenila