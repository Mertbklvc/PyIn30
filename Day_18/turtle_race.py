import turtle as t
import random

winner_besc = t.Turtle()
winner_besc.penup()
winner_besc.hideturtle()
farben_besc = t.Turtle()
farben_besc.penup()
farben_besc.hideturtle()
farben_besc.goto(-200,250)
farben_besc.write("Red/Green/Blue/Yellow/Orange/Purple/Black",font=("Arial", 16, "bold")) 
is_race_on = False

farben = ["red", "green", "blue", "yellow", "orange", "purple","black"]

screen= t.Screen()
screen.setup(width=1000,height=800)
nutzer_bet = screen.textinput(title="Machen Sie Ihre Wette", prompt="Welche Schildkröte wird das Rennen gewinnen? Geben Sie eine Farbe ein: ")
y_position = [-150,-100,-50,0,50,100,150]
all_turtle = []

for i in range(7):
    new_turtle = t.Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(farben[i])
    new_turtle.goto(x = -480, y = y_position[i])
    all_turtle.append(new_turtle)
    
if nutzer_bet:
    is_race_on = True
while is_race_on:
    
    for turtle in all_turtle:
        if turtle.xcor() > 490:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == nutzer_bet:
                winner_besc.goto(-200,-200)  
                winner_besc.write(f"Sie haben gewinnen: {winning_color} Turtle", font=("Arial", 16, "bold"))  # Yazıyı ekrana yazdır
            else:
                winner_besc.goto(-200,-200)  
                winner_besc.write(f"Sie haben verloren! Gewinnen: {winning_color} Turtle", font=("Arial", 16, "bold"))  # Yazıyı ekrana yazdır

        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)
    















screen.exitonclick()
