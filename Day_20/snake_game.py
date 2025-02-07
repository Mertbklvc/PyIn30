from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time 
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)




food = Food()
snake = Snake()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

    
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
  
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        game_is_on = False
        scoreboard.game_over() 



    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over(),

screen.exitonclick()
