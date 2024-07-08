"""recursion tree drawing"""
import random as rd
import turtle

def tree(branch_len,t):
    """drawing tree"""
    amin = 15
    amax = 40
    ang: int = rd.randrange(amin, amax)
    lmin = 8
    lmax = 20
    l: int = rd.randrange(lmin, lmax)
    t.pensize(branch_len//10)
    if branch_len > 5:
        t.forward(branch_len)
        t.right(ang)
        tree(branch_len-l,t)
        t.left(2*ang)
        tree(branch_len-l,t)
        t.right(ang)
        if branch_len//10 <=1:
            t.pensize(1)
            t.color('green')
        else:
            t.color('brown')
        t.backward(branch_len)

def main():
    """main"""
    t = turtle.Turtle()
    t.speed(5)
    t.color('brown')
    mywin = turtle.Screen()
    mywin.tracer(2)
    t.left(90)
    t.up()
    t.backward(150)
    t.down()

    tree(90,t)
    mywin.exitonclick()

if __name__ == '__main__':
    main()
