import turtle

#kilpkonna seaded
turtle.speed(0)
ekraan = turtle.Screen()
ekraan.title("Olümpiarõngad - Erik")
ekraan.setup(500,400)





#olümpiarõngad
turtle.pencolor("blue")
turtle.pensize(6)
turtle.penup()
turtle.goto(-110,0)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("black")
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("red")
turtle.penup()
turtle.goto(110,0)
turtle.pendown()
turtle.circle(50)


turtle.pencolor("yellow")
turtle.penup()
turtle.goto(-55,-45)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("green")
turtle.penup()
turtle.goto(55,-45)
turtle.pendown()
turtle.circle(50)


turtle.done()