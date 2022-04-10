import turtle
import time
from collections import deque
from Maze import getMaze

maze_width = 25

win = turtle.Screen()
win.bgcolor('white')
win.setup(550, 550)

def endProgram():
    win.exitonclick()

# Class for Maze blocks
class MazeGUI(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape('square')
        self.color('black')
        self.penup()
        self.goto(-550,-550)

# Class for End Blocks
class EndGUI(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color('green')
        self.shape('square')
        self.speed(0)
        self.penup()
        self.goto(-550, -550)

# Class for Blue PathFinding Blocks
class PathFinderGUI(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color('blue')
        self.shape('square')
        self.speed(0)
        self.penup()
        self.goto(-550, -550)

# Class for the Path of Mouse
class PathGUI(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color('yellow')
        self.shape('square')
        self.speed(0)
        self.penup()
        self.goto(-550, -550)

# Class for the Mouse
class MouseGUI(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color('red')
        self.shape('circle')
        self.speed(0)
        self.penup()
        self.goto(-550, -550)

def setupMaze(mazeDesign, MazeGUI, EndGUI, MouseGUI):
    walls = []
    global start_x, start_y, end_x, end_y       # defining Global variable for start and end
    for row in range(len(mazeDesign)):
        for col in range(len(mazeDesign[row])):
            character = mazeDesign[row][col]
            screen_x = -255 + (col * maze_width)
            screen_y = 255 - (row * maze_width)

            if character == '*':
                MazeGUI.goto(screen_x, screen_y)
                MazeGUI.stamp()
                walls.append((screen_x, screen_y))

            elif character == 'E':
                EndGUI.goto(screen_x, screen_y)
                EndGUI.stamp()
                end_x, end_y = screen_x, screen_y          # End Points

            elif character == 'S':
                MouseGUI.goto(screen_x, screen_y)
                start_x, start_y = screen_x, screen_y       # Starting Points




    return walls

def search(x, y, walls, PathFinderGUI):
    solution = {}
    visited = set()
    frontier = deque()
    frontier.append((x,y))
    solution[x,y] = x,y

    while len(frontier) >= 1:
        x, y = frontier.popleft()       # Move 1st element of frontier to Current

        # check if cell on the Left is empty and movable
        if (x - maze_width, y) not in walls and (x - maze_width, y) not in visited:
            cell = (x - maze_width, y)
            frontier.append(cell)
            visited.add(cell)
            solution[cell] = x,y

        # check if cell on the Right is empty and movable
        if (x + maze_width, y) not in walls and (x + maze_width, y) not in visited:
            cell = (x + maze_width, y)
            frontier.append(cell)
            visited.add(cell)
            solution[cell] = x,y

        # check if cell Below is empty and movable
        if (x, y - maze_width) not in walls and (x, y - maze_width) not in visited:
            cell = (x, y - maze_width)
            frontier.append(cell)
            visited.add(cell)
            solution[cell] = x,y

        # check if cell on the left is empty and movable
        if (x, y + maze_width) not in walls and (x, y + maze_width) not in visited:
            cell = (x, y + maze_width)
            frontier.append(cell)
            visited.add(cell)
            solution[cell] = x,y

        PathFinderGUI.goto(x, y)
        PathFinderGUI.stamp()

        if (x,y) == (end_x, end_y):     # Stop checking of cells if we find the Target
            break
        time.sleep(0.02)

    return solution

def BackTrack(x, y, solution, PathGUI):
    path_sol = []
    path_sol.append((x,y))
    PathGUI.goto(x, y)
    PathGUI.stamp()
    while (x, y) != (start_x, start_y):        # Run the loop till the current x,y becomes starting x,y
        next = solution.get((x,y))
        PathGUI.goto(next)
        PathGUI.stamp()
        path_sol.append(next)
        x, y = next
        time.sleep(0.05)

    return path_sol

def GetMousetoEnd(path_sol, Mouse):        # GUI to animate Mouse going to end
    path_sol.reverse()
    for count in path_sol:
        Mouse.goto(count)
        time.sleep(0.1)
    endProgram()

# Class Objects
maze = MazeGUI()
end = EndGUI()
mouse = MouseGUI()
pathGui = PathGUI()
pathFinder = PathFinderGUI()

#################MAIN PROGRAM###################
walls = setupMaze(getMaze(), maze, end, mouse)
time.sleep(0.5)
solution = search(start_x, start_y, walls, pathFinder)
# setupMaze(getMaze(), maze, end, mouse)        # For Aesthetical Purposes
time.sleep(0.5)
path_sol = BackTrack(end_x, end_y, solution, pathGui)
time.sleep(0.5)
GetMousetoEnd(path_sol, mouse)
