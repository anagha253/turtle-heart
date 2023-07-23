import turtle

def lh():
    turtle.fd(11)
    turtle.circle(50,180)
    turtle.left(12)
    turtle.fd(180)

def rh():
    turtle.left(55)
    turtle.fd(150)
    turtle.circle(50,180)
    turtle.fd(20)

def heart():
    turtle.pencolor("red")
    turtle.speed(1)
    turtle.color("red")
    turtle.begin_fill()
    rh()
    turtle.right(120)
    lh()
    turtle.end_fill()

heart()