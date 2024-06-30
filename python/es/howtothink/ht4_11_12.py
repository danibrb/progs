"""draw regular polygon"""

import turtle as t

wn = t.Screen()
ciro = t.Turtle()

s = int(input("enter sides: "))

for i in range(s):
    ciro.fd(60)
    ciro.lt(360/s)

wn.exitonclick()
