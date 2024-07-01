"""calculating pi value using monte carlo simulation"""
import turtle
import random

fred = turtle.Turtle()

WN = turtle.Screen()
WN.setworldcoordinates(-1,-1,1,1)
WN.bgcolor("lightgreen")
WN.tracer(100)
fred.color("blue")
fred.shape("circle")
fred.shapesize(0.3)
fred.speed("fast")
fred.up()

NDART = 2000
count: int = 0
for i in range(NDART):
    randx = random.random()
    randy = random.random()

    x = randx*2.0 - 1
    y = randy*2.0 - 1
    fred.goto(x,y)
    if fred.distance(0,0) <=1 :
        fred.color("red")
        count += 1
    else:
        fred.color("blue")
    fred.stamp()

pi: float = count/NDART*4

print(f"n of trows: {NDART} pi value: {pi}")

WN.exitonclick()
