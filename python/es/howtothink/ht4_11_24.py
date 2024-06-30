"""draw a face of a clock"""
import turtle as t

WD = t.Screen()
WD.bgcolor("green")
p = t.Turtle()
p.width(3)
p.color("blue")
p.shape("turtle")

p.up()

for i in range(12):
    p.fd(80)
    p.down()
    p.fd(10)
    p.up()
    p.fd(10)
    p.stamp()
    p.bk(100)
    p.rt(30)

WD.exitonclick()
