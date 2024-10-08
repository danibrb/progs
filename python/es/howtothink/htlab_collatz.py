"""collatz conjecture"""
import turtle

WD = turtle.Screen()
WD.setworldcoordinates(0,0,50,120)
t= turtle.Turtle()
t.speed("fast")


def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    count = 0
    while n != 1:
        #print(n)
        count += 1
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    #print(n)                  # the last print is 1
    return count

for start in range(1,51):
    step: int = seq3np1(start)
    print(f"number: {start} iterations: {step}")
    t.goto(start,step)

WD.exitonclick()
