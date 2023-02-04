import turtle
import random

x=turtle.Turtle()
x.penup()
x.goto(-300,200)
x.pendown()
x.shape("turtle")
x.color("red")


y=turtle.Turtle()
y.penup()
y.goto(-300,100)
y.pendown()
y.shape("turtle")
y.color("green")

for i in range(20):
    if x.pos()>=(300,100):
        print("PLayer1 wins")
        break
    elif y.pos()>=(300,100):
        print("player 2 wins")
        break
    else:
        d=[1,2,3,4,5,6]
        z=int(input("enter no for player 1"))
        a=int(input("enter no for player 2"))
        x.fd(20*z)
        y.fd(20*a)
