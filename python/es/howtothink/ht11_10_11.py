"""turtle best fit"""

import turtle

def mean(lst: list[float]) -> float:
    """calculate mean from a list of data"""
    s = 0
    for n in lst:
        s += n
    return s/len(lst)


def mc(x: list[float] , y: list[float]) -> float:
    """calculate m coefficient"""
    sn = 0
    sd = 0
    n = len(x)
    for i in range(n):
        sn += x[i]*y[i] - n*mean(x)*mean(y)
        sd +=  x[i]**2 - n*mean(x)**2
    return sn/sd    
    
def main():
    """main function"""
    xd: list[float] = []
    yd: list[float] = []

    with open("python/es/howtothink/labdata.txt", "r", encoding="utf8") as f:

        for aline in f:
            items = aline.split()
            #convert str into float
            xd.append(float(items[0]))
            yd.append(float(items[1]))


    b = 5
    xmin = min(xd)
    xmax = max(xd)
    ymin = min(yd)
    ymax = max(yd)
    wd = turtle.Screen()
    wd.setworldcoordinates(xmin-b, ymin-b, xmax+b, ymax+b)

    t = turtle.Turtle()
    t.speed(10)
    t.shape("circle")
    t.shapesize(0.2)
    t.up()

    n = len(xd)
    for i in range(n):
        t.goto(xd[i], yd[i])
        t.stamp()
    
    xm = mean(xd)
    ym = mean(yd)
    m = mc(xd, yd)
    
    t.goto(xmin, ymin)
    t.down()
    t.color('blue')
    for x in range(int(xmin),int(xmax)):
        y = ym + m*(x - xm)
        t.goto(x, y)

    wd.exitonclick()

if __name__ == '__main__':
    main()
