import turtle 

zelva = turtle.Turtle()
zelva.speed(0)


screen = turtle.Screen()
screen.title = "black niggers"
screen.bgcolor = "black"
screen.setup(width=800, height=600)


def forward():
    zelva.setheading(0)
    zelva.forward(100)

def leva():
    zelva.left(90)
    zelva.forward(100)

def desna():
    zelva.right(90)
    zelva.forward(100)

def back():
    zelva.back(100)

def reset():
    screen.clear()
    zelva.home()

def niggerkotnik():
    zelva.home()
    for i in range(10):
        zelva.forward(45)
        zelva.left(30)
def krogc():
    r = 1
  
    n = 100
    
    for i in range(1, n + 1, 1):
        zelva.circle(r * i)


screen.onkey(forward, "w")
screen.onkey(leva, "a")
screen.onkey(desna, "d")
screen.onkey(back, "s")
screen.onkey(reset, "r")
screen.onkey(niggerkotnik, "n")
screen.onkey(krogc, "k")

screen.listen()



turtle.done()

