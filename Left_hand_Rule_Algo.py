import turtle
import sys
import time
from Maze import getMaze

maze_width = 25

win = turtle.Screen()
win.bgcolor('white')
win.setup(550, 550)


def endProgram():
    win.exitonclick()
    sys.exit()


# Class for Maze(Turtle)
class MazeSpec(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color('black')
        self.shape('square')
        self.penup()
        self.speed(0)


# Class for EndGUI Marker
class EndSpec(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('green')
        self.penup()
        self.speed(0)


# class for Rat (MouseGUI)
class miniMouse(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('arrow')
        self.color('red')
        self.setheading(180)
        self.penup()
        self.speed(0)

    def MouseMove(self, walls, finish):
        x_cor = round(self.xcor())
        y_cor = round(self.ycor())
        if (x_cor, y_cor) in finish:
            print('Phoch gaya re Apun...😎😎')
            endProgram()

        flag = False  # this variable is to keep track if there is wall on the left
        if self.heading() == 0:  # Facing Left
            if (x_cor, y_cor + maze_width) in walls:  # Check if there are walls on the Left
                flag = True
                if (x_cor + maze_width, y_cor) not in walls:
                    self.fd(maze_width)
                else:
                    self.rt(90)

        elif self.heading() == 90:  # Facing Up
            if (x_cor - maze_width, y_cor) in walls:  # Check if there are walls on the Left
                flag = True
                if (x_cor, y_cor + maze_width) not in walls:
                    self.fd(maze_width)
                else:
                    self.rt(90)

        elif self.heading() == 180:  # Facing Right
            if (x_cor, y_cor - maze_width) in walls:  # Check if there are walls on the Left
                flag = True
                if (x_cor - maze_width, y_cor) not in walls:
                    self.fd(maze_width)
                else:
                    self.rt(90)

        elif self.heading() == 270:  # Facing Down
            if (x_cor + maze_width, y_cor) in walls:  # Check if there are walls on the Left
                flag = True
                if (x_cor, y_cor - maze_width) not in walls:
                    self.fd(maze_width)
                else:
                    self.rt(90)

        if flag == False:
            self.lt(90)
            self.fd(maze_width)


def setupMaze(mazeDesign, miniMouse, Maze, End):
    walls = []
    finish = []

    for row in range(len(mazeDesign)):
        for col in range(len(mazeDesign[row])):
            character = mazeDesign[row][col]
            screen_x = -255 + (col * maze_width)
            screen_y = 255 - (row * maze_width)

            if character == '*':
                Maze.goto(screen_x, screen_y)
                Maze.stamp()
                walls.append((screen_x, screen_y))
            if character == 'S':
                miniMouse.goto(screen_x, screen_y)
            if character == 'E':
                End.goto(screen_x, screen_y)
                End.stamp()
                finish.append((screen_x, screen_y))

    return walls, finish


###############MAIN PROGRAM####################

mouse = miniMouse()
Maze = MazeSpec()
End = EndSpec()
mazeDesign = getMaze()

walls, finish = setupMaze(mazeDesign, mouse, Maze, End)

while True:
    mouse.MouseMove(walls, finish)

    time.sleep(0.2)
