import turtle

# Kirjuta programm, mis kasutab Turtle graafikat joonistamaks ringi ning arvutab ja kuvab konsoolis ringi pindala ja ümbermõõdu.
# Programm küsib kasutajalt ringi raadiuse.
# Kasuta ** operaatorit raadiuse ruudu arvutamiseks ja π väärtusena 3.14.
# Lisa veakontroll, et kontrollida kasutaja sisestatud raadiuse korrektsust.
# Väljasta lause, kasutades f-string vormindamist ja ümardamist 2 komakohta
# Näide:
# Kasutaja sisestab: 5
# Programm väljastab konsoolis: Ringi pindala on 78.5 ja ümbermõõt on 31.4
# Turtle graafika joonistab vastava ringi

try:
    r = float(input("Ringi raadius r="))
    s = 3.14 * r ** 2
    p = 2 * 3.14 * r
    print(f"Ringi pindala on {s:0.2f} ja ümbermõõt on {p:.2f}")
    turtle.circle(r)
except:
    print("Kontrolli sisestust!")













turtle.done()