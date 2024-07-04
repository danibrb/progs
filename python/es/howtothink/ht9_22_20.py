"""L-system arrowhead curve"""
import turtle

def createLSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for _i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'X':
        newstr = 'YF+XF+Y'   # Rule 1
    elif ch == 'Y':
        newstr = 'XF-YF-X'
    else:
        newstr = ch     # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main():
    inst = createLSystem(7, "YF")  # create the string, odd numbers pointing up
    print(inst)
    t = turtle.Turtle()           # create the turtle
    wn = turtle.Screen()
    #wn.screensize(1000,1000)
    #speed up drawing
    wn.tracer(10)
    #hiding turtle
    t.ht()

    t.up()
    t.goto(-250,-250)
    t.down()
    t.speed(0)
    drawLsystem(t, inst, 60, 4)   # draw the picture
                                    # angle 60, segment length 5
    wn.exitonclick()

main()