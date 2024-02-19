import turtle 

w = turtle.Screen()
w.title("PONG")
w.bgcolor("orange")
w.setup(width=800, height=600)
w.tracer(0)

scorea = 0
scoreb = 0

paddlea = turtle.Turtle()
paddlea.speed(0)
paddlea.shape("square")
paddlea.shapesize(stretch_wid= 5, stretch_len=1)
paddlea.color("black")
paddlea.penup()
paddlea.goto(-350, 0)


paddleb = turtle.Turtle()
paddleb.speed(0)
paddleb.shape("square")
paddleb.shapesize(stretch_wid= 5, stretch_len=1)
paddleb.color("black")
paddleb.penup()
paddleb.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2




def aup():
    y= paddlea.ycor()
    y+= 20
    paddlea.sety(y)

def ad():
    y= paddlea.ycor()
    y-= 20
    paddlea.sety(y)


def bup():
    y= paddleb.ycor()
    y+= 20
    paddleb.sety(y)

def bd():
    y= paddleb.ycor()
    y-= 20
    paddleb.sety(y)


w.listen()
w.onkeypress(aup, "q")
w.onkeypress(ad, "a")
w.onkeypress(bup, "Up")
w.onkeypress(bd, "Down")


while True:
    w.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scorea += 1
        pen.clear()
        pen.write("A:{}  B:{}".format(scorea, scoreb), align= "center", font=("Courier", 24, "normal"))

    if ball.xcor() <  -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreb += 1
        pen.clear()
        pen.write("A: {}  B: {}".format(scorea, scoreb), align= "center", font=("Courier", 24, "normal"))

    
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("Black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.clear()
    pen.write("A:0  B:0", align= "center", font=("Courier", 24, "normal"))



    if (ball.xcor()> 340 and ball.xcor() < 350 ) and (ball.ycor()< paddleb.ycor()+40 and ball.ycor() > paddleb.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
    
    
    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor() < paddlea.ycor()+40 and ball.ycor() > paddlea.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1

