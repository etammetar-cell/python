# Kingituste pakkimine
# Sa töötad kingipoes ja sinu ülesanne on pakkida kingitusi.
# Igasse kinkekarpi mahub täpselt 5 kingitust.
# Sinu ülesandeks on arvutada, mitu täis kinkekasti saad teha ja mitu kingitust jääb üle, kui need kõik ei mahu karpidesse.
# Loo programm, mis küsib kasutajalt, mitu kingitust on vaja pakkida.
# Programm peaks seejärel arvutama, mitu täis kinkekasti saab teha ja mitu kingitust jääb üle. Kasuta täisarvulist jagamist (//) kinkekarpide arvu leidmiseks ja jäägi (%) operaatorit ülejäävate kingituste arvu leidmiseks.
# Kasuta veakontrolli ja vastuse vormindamist
# Näide:
# Kasutaja sisestab: 23
# Programm väljastab: Saad teha 4 täis kinkekasti. Üle jääb 3 kingitust.


try:
    kingitused = int(input("Lisa kingituste arv: "))
    maht = 5

    kingitusi_kokku = kingitused // maht
    ylejaak = kingitused % maht

    print(f"Saad teha {kingitusi_kokku} täis kinkekasti. Üle jääb {ylejaak} kingitust.")
    
except:
    print("kontrolli sisestust")











# Raamatute allahindlus
# Raamatupoes on 30% soodusmüük.
# Kirjuta programm, mis küsib kasutajalt soovitud raamatute arvu ja arvutab nende kogumaksumuse, kui iga raamatu tavahind on 12,53€.
# Väljasta lause, kasutades f-string vormindamist ja ümardamist 2 komakohta
# Näide:
# Kasutaja sisestab: 3
# Programm väljastab: 3 raamatu hind soodustusega on 26.25€.

# ale = 0.3
# hind = 12.53
# kogus = int(input("Sisesta raamatute kogus: "))
# summa = (hind-hind*ale)*kogus
# print(f"{kogus} raamatu hind soodustusega on {summa:0.2f}€.")
# 
# 







#Aia pikkus
#Kirjuta programm, mis aitab aiapidajal arvutada aia ümbermõõtu.
#Aed on ristküliku kujuline. (a+b)*2 = P
#Programm peaks küsima kasutajalt kahe aiaosa pikkused meetrites ja seejärel arvutama aia kogupikkuse.
#Väljasta lause, kasutades f-string vormindamist.
#Näide:
#Kasutaja sisestab: 4 ja 5
#Programm väljastab: Aia kogupikkus on 18 meetrit.

#kasutaja sisestus ja muudan täisarvuks
# a = int(input("Lisa külg 1 : "))
# b = int(input("Lisa külg 2 : "))
# p = (a+b)*2
# print(f"Aia kogupikkus on {p} meetrit. ")
# 
# 











