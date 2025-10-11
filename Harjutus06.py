import turtle
import math



# Kasuta Python Turtles’i, et joonistada stseen, kus redel toetub majale 53° nurga all. Redeli ülemine ots peaks ulatuma 4,4 meetri kõrgusele maja seinal virtuaalses mõõtkavas.
# Muuda nurgad radiaanideks (radian)
# Redeli kaugus seinast: kasuta tangensfunktsiooni (tan) ja antud nurka, et leida, kui kaugele redeli alumine ots on seinast. Valem:
# Kaugus=Ko˜rgus seinaltan⁡(Nurk) 
# Redeli pikkus: kasuta Pythagorase teoreemi, et leida redeli pikkus, kui tead redeli kõrgust seinal ja kaugust seinast.
# Valem:
# Pikkus=(Ko˜rgus seinal)2+(Kaugus seinast)2 
# Ümarda vastus 2 komakohta
# Kuva vastused konsoolid
# Kasuta Python Turtles’i, et visualiseerida maantee tõusu, mis 140 meetri jooksul tõuseb 15 meetrit.
# Sinu ülesandeks on arvutada maantee tõusunurk ja näidata, kui suurt tõusu protsentides liiklusmärk enne tõusu kuvaks.
# Tõusunurga arvutamine: Kasuta tangensfunktsiooni inversi (atan), et leida tõusunurk radiaanides, ja teisenda see kraadideks.
# Nurk (kraadides) = atan(tõus/maa) × (180/π).
# Tõusu protsent: Tõusu protsent on (vertikaalne tõus / horisontaalne vahemaa) × 100.
# Ümarda täisarvuti ja kuva vastus konsoolis

nurk = 53
korgus = 4.4
radiaanid = math.radians(nurk)
kaugus = korgus / math.tan(radiaanid)
# c = math.sqrt(korgus**2+kaugus**2)
c = math.hypot(korgus,kaugus) #Sama mis eelmine
print(korgus, kaugus, c)



koef = 50 # Turtle joone pikkuse muutmiseks joonisel
turtle.fd(kaugus*koef)
turtle.lt(90)
turtle.fd(korgus*koef)
turtle.lt(90+nurk) #Sirgjoon 180kraadi siis nii lihtsam muidu turtle.lt(143)
turtle.fd(c*koef)

turtle.done()



