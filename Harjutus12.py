

#Looge funktsioon, mis võimaldab lisada või eemaldada summasid pangakontolt.
#Funktsioon peaks algama algse saldoga ja võimaldama teha operatsioone:
#  deposiit (raha lisamine) ja väljavõte (raha eemaldamine). Tagastage peale igat toimingut konto jääk.
#Funtsiooni parameetrid:
#algne_saldo: Algse saldo väärtus.
# toiming: String, mis tähistab tehtavat toimingut ('deposiit' või 'valjavote').
# summa: Summa, mida soovitakse lisada või eemaldada.
#
# 
# Näide: Alustades algse saldoga 100, deposiidi toiminguga 50, peaks funktsioon konto_haldur tagastama uue saldo 150.
#  Väljavõtte toiminguga 20 uus saldo oleks siis 130.
#Kirjutage selge dokumentatsioon, mis kirjeldab, kuidas algset saldot seada,
#  kuidas toiminguid teostada ja millist tüüpi väärtusi tagastatakse.

def konto_haldur(tehing, raha, saldo):
    """
    Lisab või eemaldab summa pangakontolt.

    Parameetrid:                                           # Dokumentatsioon konto_halduri funktsiooni jaoks
        tehing (str): Tehingutüüp.
        raha (int): Raha.
        saldo (int): Konto seis.
    Tagastab:
        int: Konto seisu.

    Näide:
    >>> algne_saldo=konto_haldur("deposiit", 50, algne_saldo)
    >>> algne_saldo=konto_haldur("maha", 100, algne_saldo)
    """












    if tehing=="deposiit":
        uus_saldo = saldo + raha
    else:
        uus_saldo = saldo - raha    
    return uus_saldo


   

algne_saldo = 100
algne_saldo=konto_haldur("deposiit", 50, algne_saldo)
algne_saldo=konto_haldur("maha", 100, algne_saldo)
algne_saldo=konto_haldur("maha", 25, algne_saldo)
algne_saldo=konto_haldur("deposiit", 10, algne_saldo)



print(algne_saldo)
print(konto_haldur.__doc__)


