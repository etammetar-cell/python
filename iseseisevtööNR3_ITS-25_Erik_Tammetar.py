

import turtle        #impordime kilpkonna
import random        #juhuslike asukohtade jaoks
                                                        #Koodijaoks kasutasin metshein.com õppematerjali,lisaks VSCode extensionid aitavad ka koodi kirjutamisel kõvasti kaasa oma eelpakkumiste ja seletustega.
screen = turtle.Screen()
screen.title("Kujundid")
t = turtle.Turtle()
t.speed(0)    #joonistuskiirus

def joonista_ruut(külg):
    for _ in range(4):
        t.forward(külg)
        t.right(90)                         # Siin on kujundid, ruut,ring,viisnurk

def joonista_ring(raadius):
    t.circle(raadius)

def joonista_viisnurk(külg):
    for _ in range(5):                            
        t.forward(külg)
        t.right(72)

while True:
    kujund = input("Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? ").strip().lower()    #kujundi küsimine
    if kujund == "":
        break

    kogus_tekst = input("Mitu kujundit soovid joonistada? (Tühi katkestab)  ").strip()   #kontroll kas sisestus oli õige
    if kogus_tekst == "":
        break 

    try:
        kogus = int(kogus_tekst)     # koguse küsimine
    except ValueError:
        print("Palun sisesta arv!")
        continue


    for _ in range(kogus):
        t.penup()    # et kilpkonn ei jätaks jälge asukohast teise liikudes
        t.goto(random.randint(-250, 250), random.randint(-200, 200))  #juhuslik asukoht
        t.pendown()  #pliiats alla et kujund joonistada

           #Joonistame vastaval valikule
        if kujund == "ruut":
            joonista_ruut(50)
        elif kujund == "ring":
            joonista_ring(30)
        elif kujund == "viisnurk":
            joonista_viisnurk(60)
        elif kujund == "suvaline":
            valik = random.choice(["ruut", "ring", "viisnurk"])
            if valik == "ruut":
                joonista_ruut(50)
            elif valik == "ring":
                joonista_ring(30)
            else:
                joonista_viisnurk(60)
        else:   
            print("Tundmatu kujund!")
        
    if input("Soovid jätkata?  (Enter lõpetab.) ").strip() == "":   #küsime kas soovib jätkata
            break
#programm lõpetab töö
print("Valmis!")
turtle.done()





