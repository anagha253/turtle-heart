import turtle
import random


turtle.bgcolor("black")
turtle.colormode(255)
turtle.speed(0)

for i in range(300):
    r,g,b=random.randint(0,255),random.randint(0,255),random.randint(0,255)
    
    turtle.pencolor(r,g,b)
    turtle.fd(i+50)
    turtle.right(121)
turtle.exitonclick()
