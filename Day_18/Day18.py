from turtle import Turtle, Screen


def verdoppeln(x):
    return x * 2

def anwenden(funktion, wert):
    return funktion(wert)

print(anwenden(verdoppeln, 5)) 

# Ein Higher-Order Function ist eine Funktion, die eine andere Funktion als Parameter nimmt oder eine Funktion zurückgibt.

mert = Turtle()
screen = Screen()



def geheVorwaerts():
    mert.forward(10)
    

screen.listen()
screen.onkey(geheVorwaerts,"space")
screen.exitonclick()


