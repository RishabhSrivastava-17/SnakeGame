from turtle import Turtle


class Scoreboard(Turtle):
	def __init__(self):
		super(Scoreboard, self).__init__()
		self.score = 0
		self.color("white")
		self.penup()
		self.goto(0, 270)
		self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
		self.hideturtle()

	def increase_score(self):
		self.score += 1
		self.clear()
		self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

	def collision(self):
		self.goto(0, 0)
		self.write("Game Over", align="center", font=("Arial", 24, "normal"))
