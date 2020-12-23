from turtle import Turtle

STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        
        self.segments = []

        for position in STARTING_POSITION:
            snake = Turtle('square')
            snake.penup()
            snake.color('white')
            snake.goto(position)    
            self.segments.append(snake)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)   
        self.segments[0].forward(MOVE_DISTANCE) 

    
    def up(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)   
        self.segments[0].setheading[90]

    def down(self):
        self.segments[0].setheading[270]

    def left(self):
        self.segments[0].setheading[180]

    def right(self):
        self.segments[0].setheading[0]