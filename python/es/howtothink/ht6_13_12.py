"""draw a spiral"""
import turtle as tu

WD = tu.Screen()
WD.bgcolor("lightgreen")
p = tu.Turtle()
p.width(1)
p.color("blue")
p.speed('fast')
#p.shape("turtle")

def draw_piece(t, sz):
    """Draw a side of spiral"""

    for dummy in range(2):  #use _ for unused variable
        t.fd(sz)
        t.rt(90)
        t.lt(2)

p.lt(180)
STEP = 10

for i in range(0,500,10):
    draw_piece(p, i+STEP)

WD.exitonclick()
