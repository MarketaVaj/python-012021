# SMS brána
# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:
#
# Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
# Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
# Tvůj program bude obsahovat dvě funkce:
#
# První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
# Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
# Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.
#
# Tip: Zkus svoji první funkci vytunit tak, že si bude umět poradit s mezerami v telefonním čísle. Mezer se zbavíš tak, že použiješ funkci replace() a tečkovou notaci. První parametr je znak, který chceš nahradit, a druhý parametr nový znak. Níže je příklad použití.
#
# tel_cislo = "+420 734 123 456"
# tel_cislo = tel_cislo.replace(" ", "")

def telefon(tel_cislo):
    tel_cislo = tel_cislo.replace(" ", "")
    if len(tel_cislo) = 9:
        cislo == True
    if len(tel_cislo) = len 12:
        cislo == True
    return cislo

def znenizpravy (zprava):
    pocetzprav = zprava/180
    cenazpravy = pocetzprav * 3
    return  cenazpravy


tel_cislo = input('Na jake cislo chcete zpravu zaslat?')
telefon (tel_cislo)
if cislo = True:
    zprava = input('Jakou zpravu chcete zaslat?')
    znenizpravy(zprava)
print('Cena zpravy je '(cenazpravy))

