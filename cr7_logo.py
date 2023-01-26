import turtle

turtle.bgcolor('black')
wop = turtle.Turtle()
wop.pencolor('white')
wop.hideturtle()

wop.penup()
wop.goto(-250, 100)
wop.pendown()

wop.color('white')
wop.begin_fill()
wop.fd(50)

wop.lt(110)

for i in range(31):
    wop.lt(10)
    wop.fd(25)

wop.lt(120)
wop.fd(50)

wop.lt(58)

for i in range(26):
    wop.rt(11)
    wop.fd(19.3)

wop.end_fill()

wop.penup()
wop.goto(-150, 183)
wop.pendown()
wop.begin_fill()
wop.rt(42)
wop.fd(287)

wop.lt(90)
wop.fd(50)

wop.lt(90)
wop.fd(250)

wop.rt(90)
wop.fd(90)

for i in range(60):
    wop.rt(3)
    wop.fd(3)

wop.fd(85)

wop.lt(130)
wop.fd(180)

wop.lt(50)
wop.fd(55)

wop.lt(130)
wop.fd(134)

wop.rt(130)
wop.fd(17)


for i in range(60):
    wop.lt(3)
    wop.fd(4.9)


wop.fd(150)
wop.end_fill()

wop.penup()
wop.goto(150, 183)
wop.pendown()
wop.begin_fill()

wop.lt(60)
wop.fd(50)

wop.lt(120)
wop.fd(150)

wop.rt(120)
wop.fd(500)

wop.lt(175)
wop.fd(580)

wop.lt(125)
wop.fd(210)
wop.end_fill()

wop.penup()
wop.goto(170, 210)
wop.pendown()
wop.begin_fill()

wop.rt(120)
wop.fd(200)

wop.rt(170)
wop.fd(185)

wop.rt(70)
wop.fd(40)
wop.end_fill()

wop.penup()
wop.goto(170, 210)
wop.pendown()

turtle.mainloop()