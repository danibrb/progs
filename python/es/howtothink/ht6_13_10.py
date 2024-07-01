"""draw a pattern"""
import turtle as tu

WD = tu.Screen()
WD.bgcolor("green")
p = tu.Turtle()
p.width(3)
p.color("blue")
p.speed('fast')
#p.shape("turtle")

def draw_square(t, sz):
    """Draw a square and rotate"""

    for dummy in range(4):  #use _ for unused variable, dummy is better
        t.forward(sz)
        t.left(90)
    t.lt(360/20)

for i in range(20):
    draw_square(p,100)

WD.exitonclick()
