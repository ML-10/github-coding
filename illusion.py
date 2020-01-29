from turtle import *
speed(-1)
bgcolor("black")
width(10)
def line():
    color("grey")
    fd(800)
    bk(2000)
    fd(1200)

def lines():
    pu()
    goto(-300,300)
    pd()
    for times in range(7):
        line()
        pu()
        rt(90)
        fd(100)
        lt(90)
        pd()


def grid():
    lines()
    lt(90)
    lines()

def dots():
    color("white")
    pu()
    goto(-300,300)
    setheading(0)
    for i in range(7):
        for i in range(7):
            dot(20)
            fd(100)
        rt(90)
        fd(100)
        lt(90)
        bk(700)

grid()
dots()

    
