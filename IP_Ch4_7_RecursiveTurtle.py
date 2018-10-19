# TODO: Create a program that writes lines out of characters
#     Extend that to use symbols (like the greek keys) to create the lines

import turtle, random

def squareSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        squareSpiral(myTurtle,lineLen-5)

def drawSquareSpiral():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    squareSpiral(myTurtle,100)
    # myWin.exitonclick()

def tree(branchLen,t):
    if branchLen > 5:
        if branchLen < 15:
            t.color('green')
        t.width(branchLen//5)
        t.forward(branchLen)
        turnAngle = random.randint(15, 45)
        t.right(turnAngle)
        tree(branchLen-random.randint(5, 15),t)
        t.left(2*turnAngle)
        tree(branchLen-random.randint(5, 15),t)
        t.right(turnAngle)
        t.backward(branchLen)
        t.color('brown')

def drawTree():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(75,t)
    myWin.exitonclick()

# http://gwydir.demon.co.uk/jo/greekkey/fractal.htm -- A repeated fractal Greek Key border
# 9x right, (r), 7x down, (r), 5x left, (r), 3x up, (r), 3x right, (l), 3x up, (l), 5x left, (l), 7x down, (l), 9x right, (l), 9x up, (r)
def drawGreekKey(t, h):
    t.forward(h*9)
    t.right(90)
    t.forward(h*9)
    t.right(90)
    t.forward(h*7)
    t.right(90)
    t.forward(h*5)
    t.right(90)
    t.forward(h*3)
    t.right(90)
    t.forward(h*3)
    t.left(90)
    t.forward(h*2)
    t.left(90)
    t.forward(h*5)
    t.left(90)
    t.forward(h*7)
    t.left(90)
    t.forward(h*9)
    t.left(90)

# To turn right (overlap) -- fwd x9, right(90) -- ADDS A SQUARE
# To turn right (no overlap) -- fwd x9, right(90), fwd x1 -- ADDS A SQUARE
def greekKeyTurnRight(t, height):
    t.forward(height*9)
    t.right(90)
    t.forward(height*2)

def greekKeyTurnLeft(t, height):
    t.forward(height*11)
    t.left(90)
    t.forward(height)

def drawGreekKeyLine(t, length, height):
    for i in range(length+1):
        drawGreekKey(t, height)

# length is the number of greekkeys that will make up each line
# height is the height of the keys themselves
# width will be proportional to the height
def drawGreekKeySquare(length, height):
#     length = 5
#     height = 4
    w = height//2
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.color('gold', 'gold')
    t.width(w)
    t.up()
#     t.goto(-600, 200)
    t.goto(-200, 200)
    t.down()
    t.left(90)
    for i in range(4):
        drawGreekKeyLine(t, length, height)
        greekKeyTurnRight(t, height)
    myWin.exitonclick()

def greekKeySquareSpiral(t, length, keyHeight):
    drawGreekKeyLine(t, length, keyHeight)
    if length > 0:
        greekKeyTurnRight(t, keyHeight)
        greekKeySquareSpiral(t, length-1, keyHeight)

def drawGreekKeySquareSpiral(length, keyHeight):
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(10)
    t.width(keyHeight//2)
    t.up()
    t.goto(-200, 200)
    t.down()
    t.left(90)
    greekKeySquareSpiral(t, length, keyHeight)
    myWin.exitonclick()

def drawCircle(t, radius, color=None):
    t.up()
    t.goto(0, -radius)
    t.down()
    if color != None:
        t.color('black', color)
        t.begin_fill()
    t.circle(radius)
    if color != None:
        t.end_fill()
        t.color('black', 'white')

# TODO: Draw greekkeys in between the two circles
def drawGreekKeyCircular():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(10)
    radius = 200
    height = (radius//2) * 0.8
    print(height)
    drawCircle(t, radius)
    drawCircle(t, radius//2, 'gold')
    myWin.exitonclick()

# drawSquareSpiral()
# drawTree()
# drawGreekKeySquare(5, 4)
drawGreekKeySquareSpiral(10, 3)
# drawGreekKeyCircular()