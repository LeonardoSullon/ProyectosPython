import turtle

def dibujar_tallo():
    turtle.color("green")
    turtle.pensize(4)
    turtle.right(90)
    turtle.circle(80, 90)
    turtle.left(90)
    turtle.pensize(4)


def dibujar_petalo():
    turtle.circle(50, 60)
    turtle.left(120)
    turtle.circle(50, 60)
    turtle.left(120)

turtle.speed(10)

turtle.penup()
turtle.goto(0, -3)
turtle.pendown()

dibujar_tallo()

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

turtle.color("yellow")
turtle.begin_fill()
for _ in range(6):
    dibujar_petalo()
    turtle.left(60)
turtle.end_fill()


def dibujar_tallo():
    turtle.color("green")
    turtle.pensize(4)
    turtle.right(200)
    turtle.circle(80, 90)
    turtle.left(90)
    turtle.pensize(4)


def dibujar_petalo():
    turtle.circle(50, 60)
    turtle.left(120)
    turtle.circle(50, 60)
    turtle.left(120)

turtle.speed(10)

turtle.penup()
turtle.goto(50, 3)
turtle.pendown()

dibujar_tallo()

turtle.penup()
turtle.goto(50, 10)
turtle.pendown()

turtle.color("yellow")
turtle.begin_fill()
for _ in range(6):
    dibujar_petalo()
    turtle.left(60)
turtle.end_fill()

def dibujar_tallo():
    turtle.color("green")
    turtle.pensize(4)
    turtle.right(160) #Angulo del tallo
    turtle.circle(80, 90) #Largo del tallo
    turtle.left(90) 
    turtle.pensize(4)


def dibujar_petalo():
    turtle.circle(50, 60)
    turtle.left(120)
    turtle.circle(50, 60)
    turtle.left(120)

turtle.speed(10)

turtle.penup()
turtle.goto(-50, 3)
turtle.pendown()

dibujar_tallo()

turtle.penup()
turtle.goto(-50, 5)
turtle.pendown()

turtle.color("yellow")
turtle.begin_fill()
for _ in range(6):
    dibujar_petalo()
    turtle.left(60)
turtle.end_fill()

turtle.exitonclick()