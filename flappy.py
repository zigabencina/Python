from tracemalloc import stop
import turtle 
import random
import time

#screen

s = turtle.Screen()

resx = 500   #int(input("Vnesi resolucijo x: "))
resy = 800  #int(input("Vnesi resolucijo y: "))

s.setup(resx,resy)

s.title("crnuhar")
s.bgcolor("white")
s.colormode(255)
s.tracer(0)

#player
player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("turtle")
player.shapesize(3)
player.color("black")
player.goto(-200,0)
sprememba_x = 0
sprememba_y = 1
g_pospesek = -0.2

#pipe gor
pipe1_top = turtle.Turtle()
pipe1_top.speed(0)
pipe1_top.penup()
pipe1_top.color("green")
pipe1_top.shape("square")
pipe1_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_top.goto(300, 250)
pipe1_x = -2
pipe1_y = 0


#pipe dol
pipe1_bottom = turtle.Turtle()
pipe1_bottom.speed(0)
pipe1_bottom.penup()
pipe1_bottom.color("green")
pipe1_bottom.shape("square")
pipe1_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_bottom.goto(300, -250)
pipe1_bottomx = -2
pipe1_bottomy = 0

def gor():

    global sprememba_y 
    sprememba_y += 7  


s.listen()
s.onkeypress(gor, "space")




#Game loop
while True:
    
    #pauza za 30fps
    time.sleep(0.02)

    #osvezitev ekrana
    s.update()

    #gravitacija
    sprememba_y += g_pospesek

    #premikanje igralca
    y = player.ycor()
    y += sprememba_y
    player.sety(y)

    if player.ycor() < -390:
        sprememba_y = 0
        player.sety(-390)

    #zgornja pipa

    x = pipe1_top.xcor()
    x += pipe1_x
    pipe1_top.setx(x) 

    #spodnja pipa

    x = pipe1_bottom.xcor()
    x += pipe1_bottomx
    pipe1_bottom.setx(x)

    if pipe1_top.xcor() < -350:
        pipe1_top.setx(350)
        pipe1_bottom.setx(350)
        pipe1_x = 1

    if pipe1_bottom.xcor() < -350:
        pipe1_bottom.setx(350)
        pipe1_top.setx(350)
        pipe1_bottomx = 1

    if player.ycor() < -380 or player.ycor() > 380:
        break    
        

    #if player.xcor() == pipe1_bottom.xcor() and player.ycor() > 300:
    #    break
        



    
    
    
    




turtle.done()




