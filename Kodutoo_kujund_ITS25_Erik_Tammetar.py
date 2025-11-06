import turtle, math

side = 200
t = turtle.Turtle()
t.hideturtle()
t.speed(0)



def ruut(nurk):
    t.penup()
    t.goto(0, 0)      # keskpunkt
    t.setheading(nurk)
    t.forward(side / math.sqrt(2))
    t.right(135)

    t.pendown()
    for _ in range(4):
        t.forward(side)
        t.right(90)

# esimene ruut (0 kraadi)
ruut(0)

# teine ruut (45 kraadi)
ruut(45)

turtle.update()
turtle.done()
