from turtle import Turtle
import encrypt_snake_game
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("./highscore.txt") as hs:
                content = hs.read()
        except:
            content = ""
        with open("./highscore.txt", "a") as hs:
            if content != "":
                content = encrypt_snake_game.dosuff(content)
            if "4532" in content:
                self.highscore = int(content.replace("4532 ", ""))
            else:
                self.highscore = 0
                hs.write(encrypt_snake_game.dosuff("4532 0"))
        self.color("green")
        self.speed(0)
        self.penup()
        self.goto(0,250)
        self.write(f"Score: {self.score}   High Score: {self.highscore}",align="center",font=('Arial', 20, 'normal'))
        self.hideturtle()
    def increase_score(self,how_much):
        self.score += how_much
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highscore}",align="center",font=('Arial', 20, 'normal'))
    def decrease_score(self,how_much):
        self.score -= how_much
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highscore}",align="center",font=('Arial', 20, 'normal'))
    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER",align="center",font=('Courier', 30, 'normal'))
    def restart(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("./highscore.txt", "w") as hs:
            hs.write(encrypt_snake_game.dosuff(f"4532 {self.highscore}"))
class RulesGiver(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.speed(0)
        self.penup()
        self.hideturtle()
    def give_rules(self):
        self.color("white")
        self.goto(0,260)
        self.write("Welcome to snake!",align="center",font=('Courier', 15, 'normal'))
        self.goto(0,230)
        self.write("The rules are simple, get the most score.",align="center",font=('Courier', 15, 'normal'))
        self.goto(0,200)
        self.write("Score will increase when you eat food.",align="center",font=('Courier', 15, 'normal'))
        self.goto(0,170)
        self.write("Use Up, Down, Right and Left arrow for controls.",align="center",font=('Courier', 15, 'normal'))
        self.goto(0,140)
        self.write("If you hit your own tail or tried to get",align="center",font=('Courier', 15, 'normal'))
        self.goto(0,110)
        self.write("out of the screen, its GAME OVER.",align="center",font=('Courier', 15, 'normal'))
        self.goto(0,80)
        self.write("Press r after game over to reset!",align="center",font=('Courier', 15, 'normal'))
        self.goto(0,50)
        self.write("Press Right arrow key to start the game.",align="center",font=('Courier', 15, 'normal'))
        self.goto(0,20)
        self.write("At anytime in the game, press q to Quit the game.",align="center",font=('Courier', 15, 'normal'))