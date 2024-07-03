from turtle import Turtle,Screen
from snake import Snake
from Score import Scoreboard
from Food import Food
import time

#formation of display screen
screen=Screen()
screen.setup(600,600)
screen.title("snake game")
screen.bgcolor("black")

#Creation of controls
screen.tracer(0)
snake=Snake()
point=Scoreboard()
food=Food()  
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

movement=True
while movement:
    screen.update()
    time.sleep(0.2)
    snake.move()

#colision with food
    if snake.head.distance(food)<15:
      food.refresh()
      snake.extend()
      point.increase_score()

#colision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
       snake.reset()
       point.reset()
       
    for segment in snake.turtles[1:]:
       if snake.head.distance(segment)<10:
          snake.reset()
          point.reset()
          
screen.exitonclick()

