import turtle
import math

p = turtle.Pen()
p.shape("turtle")
turtle.bgcolor("black")
turtle.backward(30)
turtle.position()
colors = ["blue","yellow"]

x , y = 0 , 0
r = 20
n = 3

while True:
    for j in range(len(colors)):
        p.pencolor(colors[j])
        
        for i in range(n):
            if (i == 0):
                p.left((360-((n-2)*180/n))/2)
            else:
                p.left(360/n)    
            p.forward(2*r*math.sin(math.pi/n))

        x += 10
        r += 10
        n += 1

        p.penup()
        p.setposition(x, y)  
        p.pendown()
        p.setheading(0)