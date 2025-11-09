import turtle
import time

a = turtle.Turtle()
turtle.bgcolor('red')

a.turtlesize(2)


a.color('darkgreen')
a.pensize(3)

a.speed(5)



for x in range(4):
    a.forward(200)
    a.right(90)
               
a.left(180)

for x in range(4):
    a.forward(200)
    a.right(90)

a.right(180)
a.goto(-200,-200) 
a.goto(200,200)
a.home()
a.goto(-200,200)
a.goto(200,-200)
a.right(45)
a.penup()
a.goto(220,-220)
a.left(135)
a.pendown()
for x in range(4):
    a.forward(440)
    a.left(90)


turtle.done()