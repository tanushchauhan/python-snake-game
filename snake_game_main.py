from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard, RulesGiver
import time
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game :)")
screen.tracer(0)
def main():
    global snake
    snake = Snake()
    rules = RulesGiver()
    rules.give_rules()
    screen.listen()
    screen.update()
    def start_game():
        global food
        global scoreboard
        global game_is_on
        game_is_on =True
        rules.clear()
        rules.hideturtle()
        food = Food()
        scoreboard = ScoreBoard()
        screen.onkey(snake.left, "Left")
        screen.onkey(snake.right, "Right")
        screen.onkey(snake.Up, "Up")
        screen.onkey(snake.Down, "Down")
        while game_is_on:
            time.sleep(0.1)
            screen.update()
            snake.move()
            if snake.head.distance(food) < 15:
                scoreboard.increase_score(1)
                food.refresh()
                snake.increase_size(1)
            if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
                scoreboard.game_over()
                game_is_on = False
            for i in snake.body[1:]:
                # if i == snake.body[0]:
                #     continue
                if i.distance(snake.body[0]) < 10:
                    scoreboard.game_over()
                    game_is_on = False
    screen.onkey(start_game, "Right")
def restart_game():
    if game_is_on:
        return None
    snake.clear()
    snake.reset()
    scoreboard.clear()
    scoreboard.reset()
    scoreboard.restart()
    scoreboard.hideturtle()
    food.clear()
    food.reset()
    food.hideturtle()
    screen.update()
    main()
def exit_the_game():
    global game_is_on
    game_is_on = False
    exit()
screen.onkey(restart_game, "r")
screen.onkey(exit_the_game, "q")
main()
screen.mainloop()