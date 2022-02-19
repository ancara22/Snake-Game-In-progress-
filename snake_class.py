from turtle import Turtle, Screen
import time

class Snake:
	def __init__(self):
		self.start_positions = []
		self.turtles = []
		self.window = Screen()

	def set_window(self, bg_color, width, height):
		self.window.setup(width=width, height=height)
		self.window.bgcolor(bg_color)
		self.window.tracer(0)

	def positions_update(self):
		if len(self.start_positions) == 0:
			self.start_positions = [(0, 0), (-20, 0), (-40, 0)]
		else:
			if len(self.turtles) == 0:
				self.update_segments()
			else:
				self.start_positions = []
				for i in self.turtles:
					self.start_positions.append(i.pos())

		print(self.start_positions) ######


	def add_segments(self):
		food = True
		if food:
			pos1_x = self.start_positions[-1][0]
			pos1_y = self.start_positions[-1][1]
			pos2_x = self.start_positions[-2][0]
			pos2_y = self.start_positions[-2][1]
			res_x = pos1_x - pos2_x
			res_y = pos1_y - pos2_y
			c_x = pos1_x + res_x
			c_y = pos1_y + res_y
			coord = (c_x, c_y)
			self.start_positions.append(coord)
			#self.update_segments()



	def update_segments(self):
		for position in self.start_positions:
			new_turt = Turtle("square")
			new_turt.color("white")
			new_turt.penup()
			new_turt.goto(position)
			self.turtles.append(new_turt)

	def left(self):
		self.turtles[0].left(90)

	def right(self):
		self.turtles[0].right(90)

	def move(self):
		game_over = True
		while game_over:
			self.window.update()
			time.sleep(0.2)
			self.positions_update()
			self.add_segments()
			for segment_nr in range(len(self.turtles) - 1, 0, -1):
				self.turtles[segment_nr].goto(self.turtles[segment_nr - 1].pos())
			self.turtles[0].forward(20)
			self.window.listen()
			self.window.onkey(self.left, "Left")
			self.window.onkey(self.right, "Right")
			self.window.onkey(self.add_segments, "Down")




