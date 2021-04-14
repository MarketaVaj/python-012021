# Twilio
# Stáhni si soubor twlo.csv, který obsahuje informace o vývoji ceny akcie firmy Twilio od začátku roku 2020. Soubr obsahuje informace o otevírací, minimální, maximální a uzavírací ceně za každý den.
#
# Stažení souboru pomocí wget:
#
# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")
# Zjisti, kolik má soubor řádek a kolik sloupců.
# U akcií nás zajímají především nejnovější ceny. Podívej se na poslední řádek souboru.
# Podívej se na 5 řádků s cenami na začátku souboru, využij k tomu funkci iloc i funkci head().
# Tentokrát využij způsob dle vlastního výběru :-)
# Dobrovolný doplněk
#
# Tato část je jen doplnění, k získání bodu je potřeba zpracovat i dotazy výše :-)
#
# Počet řádků ulož do proměnné pocet_radku jako číslo.
# Pokud funkci iloc zadáš číslo řádku i číslo sloupce, odkazuješ se na jednu konkrétní hodnotu. Pandas ti tuto hodnotu vrací jako číslo. Načti si tedy první hodnotu zavírací ceny (sloupec Close) v souboru a poslední hodnotu zavírací ceny v souboru. Vypočítej, o kolik procent se zvýšila hodnota akcie.
# Vyber si sloupec s maximální cenou akcie (sloupec High) za jednotlivé dny pomocí loc nebo iloc jako sérii. Na sloupec použij funkci .max(), abys zjistila maximální zaznamenanou cenu akcie za celé období. Obdobným způsobem použij funkci .min() na sloupec Low. Z těchto hodnot zjistíš maximální rozsah obchodní ceny akcie, což je základ jednoho z akciových ukazatelů (price range).

import pandas
# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

akcie = pandas.read_csv("twlo.csv")

print(akcie.info())
# print(akcie.shape)

# print(akcie.head())
# print(akcie.iloc[:5])

# print(akcie.tail(n=1))
# print(akcie.iloc[-1:])

# pocet_radku=akcie.shape[0]
# print(pocet_radku)

# print(akcie.loc[[0,301],'Close'])
#
# akcie1 = int(akcie.loc[[0],'Close'])
# akcie2 = int(akcie.loc[[301],'Close'])
# vypocet = (akcie2 - akcie1)/akcie1 *100
# print("Cena se zvysila o ", (vypocet) ,"procent.")


# Vyber si sloupec s maximální cenou akcie (sloupec High) za jednotlivé dny pomocí loc nebo iloc jako sérii. Na sloupec použij funkci .max(), abys zjistila maximální zaznamenanou cenu akcie za celé období. Obdobným způsobem použij funkci .min() na sloupec Low. Z těchto hodnot zjistíš maximální rozsah obchodní ceny akcie, což je základ jednoho z akciových ukazatelů (price range).

maximum = akcie.loc[:,["High"]]
hodnotamax = int(maximum.max())
print('Maximalni hodnota je: ',(hodnotamax))

minimum = akcie.loc[:,["Low"]]
hodnotamin = int(minimum.min())
print('Minimalni hodnota je: ', (hodnotamin))

pricerange = hodnotamax - hodnotamin
print('Price range je: ',(pricerange))