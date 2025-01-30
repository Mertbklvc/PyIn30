import turtle as t
import random

mert = t.Turtle()
mert.shape("arrow")
mert.color("black")
farbe = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
directions = [0,90,180,270]
mert.pensize(10)
screen = t.Screen()
screen.colormode(255)
for i in range(4):
    mert.forward(100)
    mert.right(90)

screen.clear()

for i in range(10):
    mert.forward(10)
    mert.penup()
    mert.forward(10)
    mert.pendown()
    

screen.clear()
mert.home()


for i in range(20):
    mert.color(random.choice(farbe))
    mert.forward(50)
    mert.setheading(random.choice(directions))
    




screen.clear()
mert.home()






screen.exitonclick()
