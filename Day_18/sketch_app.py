import turtle as t

stift = t.Turtle()
screen = t.Screen()

def move_forward():
    stift.forward(10)
    
    
def move_backward():
    stift.backward(10)

def move_left():
    new_heading = stift.heading() + 10
    stift.setheading(new_heading)
    
def move_right():
    new_heading = stift.heading() - 10
    stift.setheading(new_heading)
    

def clear():
    stift.clear()
    stift.penup()
    stift.home()
    stift.pendown()
    
    
screen.listen()
screen.onkeypress(move_forward,"w")
screen.onkeypress(move_left,"a")
screen.onkeypress(move_right,"d")
screen.onkeypress(move_backward,"s")
screen.onkey(clear,"c")
screen.exitonclick()