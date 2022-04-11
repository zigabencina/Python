import turtle 
from random import randint

s = turtle.Screen()

resx = 800   #int(input("Vnesi resolucijo x: "))
resy = 800  #int(input("Vnesi resolucijo y: "))

s.setup(resx,resy)

s.title("crnuhar")
s.bgcolor("gray")
s.colormode(255)
tb = turtle.Turtle()
tw = turtle.Turtle()
tb.speed(0)
tw.speed(0)

position1 = 400
position2 = 300


def black_square():
    tb.pendown()
    tb.begin_fill()
    for i in range(4):
        tb.forward(100)
        tb.right(90)
    tb.end_fill()
    tb.penup()

def white_square():
    tw.shape("square")
    tw.color("white")
    tw.pendown()
    tw.begin_fill()
    for i in range(4):
        tw.forward(100)
        tw.right(90)
    tw.end_fill()
    tw.penup()

tb.penup()
tw.penup()
tb.shape("square")
tw.color("black")
tb.color("black")
tw.shape("square")
tb.goto(-400,position1)
tw.goto(-300,position1)

for u in range(3):
    for i in range(4):
        black_square()
        tb.forward(200)  
        white_square()
        tw.forward(200)
    position1 -= 200
    tb.goto(-400,position1)
    tw.goto(-300,position1)

for o in range(5):
    for n in range(4):
        white_square()
        tw.forward(200)  
        black_square()
        tb.forward(200)
    tw.goto(-400,position2)
    tb.goto(-300,position2)
    position2 -= 200


        
        




turtle.done()