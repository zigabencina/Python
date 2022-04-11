import turtle

from random import randint



s = turtle.Screen()

s.title('En kup enih želv')

s.bgcolor('black')

s.colormode(255)

s.setup(800, 600)



zelve = []



for i in range(100):

    t = turtle.Turtle()

    t.up()

    t.speed(0)

    t.shape('circle')

    t.color('white', (randint(0, 255), randint(0, 255), randint(0, 255)))

    t.goto(randint(-400, 400), randint(-300, 300))


    zelve.append(t)



gravitacija = 3

pospesek = 1



while True:



    for zelva in zelve:

        zelva.sety(zelva.ycor() - gravitacija)



        if zelva.ycor() < -300:

            zelva.sety(-285)



    gravitacija = gravitacija + pospesek



turtle.done()