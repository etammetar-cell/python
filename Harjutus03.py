import turtle


nimi = "Juhan"
vanus = 58
pikkus = 1.80

print(nimi)
print(vanus, pikkus)
#“Karin , 18 aastat vana ja keskmine hinne on 4.7”

print(nimi,",", vanus, "aastat vana ja pikkus on", pikkus, "m")

print(nimi+", "+str(vanus)+ " on aastat vana ja pikkus on "+str(pikkus)+ "m")

# Loo muutuja sihtkoht, mis sisaldab reisi sihtkohta (string)
# Loo muutuja paevade_arv, mis näitab, mitu päeva reis kestab (integer)
# Loo muutuja oobimise_hind, mis näitab ühe öö hinna (float)
# Trüki välja lause, mis ühendab need andmed, nt: “Soome reis kestab 5 päeva ja üks öö maksab 30.50 eurot.”
# Kasuta väljatrükkimisel ainult komasid (,)

sihtkoht = "Haapsalu"
paevade_arv = 5
oobimise_hind = 100.50
kokku = paevade_arv * oobimise_hind

print(sihtkoht,"reis kestab", paevade_arv,"päeva ja maksab kokku",kokku,"€")

# Loo muutuja kylje_pikkus, mis määrab kujundi külje pikkuse (täisarv)
# Loo muutuja nurk, mis määrab kujundi nurga (täisarv)
#Loo muutuja kujundi_varv, mis määrab kujundi joonevärvi (string)
#Kasutades Turtle’i, joonista kõrvuti 3 värvilist ruutu, mis kasutab loodud muutujaid
#Iga ruut on järgmisest 1,5 korda eemal
#Testi: muuda külje pikkust ning ruudud on kenasti teineteisest eemal

kylje_pikkus = 100
nurk = 90
kujundi_varv= "blue"
x = 110
kordaja = x * 1.5

turtle.pencolor(kujundi_varv)


for j in range(3):
    for i in range (4):
        turtle.fd(kylje_pikkus)
        turtle.lt(nurk)
    turtle.penup()
    turtle.goto(x,0)
    turtle.pendown()
    x = x * 2
        





turtle.done

