from mujibfunctions import *

turtle.bgcolor("purple")
turtle.colormode(255)
turtle.tracer(False)
bob.speed(0)
bob.shape("triangle")
for time in range(300):
    bob.pu()
    bob.forward(time)
    bob.left(37)
    bob.pd()
    bob.stamp()
    bob.left(15)
    tile("gold")
turtle.tracer(True)
