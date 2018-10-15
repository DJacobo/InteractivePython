# ====================================================================== MySolution
# Takes the length of a side of the largest triangle
# Draws that triangle
#     Records the "Top corners" of each of the three inner triangles
#         (one of which is the very same as the current top)
#     Draws the inner, inverted, triangle that splits the triangle into three
#     Recursively calls to fill the inner three triangles starting at their respective top corners
# ====================================================================== Book Solution
# The first thing sierpinski does is draw the outer triangle.
# Next, there are three recursive calls, one for each of the new corner triangles we get when we connect the midpoints.

# sierpinski works its way to the smallest allowed triangle in the lower-left corner,
#   and then begins to fill out the rest of the triangles working back.
# Then it fills in the triangles in the top corner by working toward the smallest, topmost triangle.
# Finally, it fills in the lower-right corner, working its way toward the smallest triangle in the lower right
# The sierpinski function relies heavily on the getMid function.
# getMid takes as arguments two endpoints and returns the point halfway between them.

# In addition, ActiveCode 1 has a function that draws a filled triangle using the begin_fill and end_fill turtle methods
# ===================================================================== Differences
# Adding the begin_fill function makes the resulting image nicer to look at
#     TODO: Add a "colormap" like the book did
# My version requires only a length and a number of iterations, making it much more user-friendly
# My version operates through distance from a starting position, and not between points.
#     This results in more code to achieve the same result

import turtle, math

myTurtle = turtle.Turtle()
myTurtle.speed(0)
window = turtle.Screen()
colormap = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

def drawSierpinskiTriangle(length, iterations):
    if length < 0:
        raise ValueError('Length cannot be negative')
    # Draw the outer triangle according to the desired length
    drawOuterTriangle(length)
    if iterations > 0:
        myTurtle.color('black', colormap[iterations])
        # Make note of all subsequent corner positions
        midCorner = (0, length//2)
        diff = getHeightDiff(midCorner, length//2)
        leftPos = (-length//4, midCorner[1]-diff)
        rightPos = (length//4, midCorner[1]-diff)
        if iterations > 1:
            # Draw inverse triangle
            drawMidpointsTriangle(midCorner, length)
            # Recursively continue
            drawRecursive(midCorner, length//2, iterations-1)
            drawRecursive(leftPos, length//2, iterations-1)
            drawRecursive(rightPos, length//2, iterations-1)
        # Wait for user to exit
    window.exitonclick()

def drawRecursive(topPos, length, iterations):
    myTurtle.up()
    myTurtle.goto(topPos)
    myTurtle.seth(90)
    topCorner = topPos
    myTurtle.color('black', colormap[iterations])
    diff = getHeightDiff(topCorner, length//2)
    leftPos = (topPos[0]-length//4, topPos[1]-diff)
    rightPos = (topPos[0]+length//4, topPos[1]-diff)
    drawMidpointsTriangle(topCorner, length)
    if iterations > 0:
        drawRecursive(topCorner, length//2, iterations-1)
        drawRecursive(leftPos, length//2, iterations-1)
        drawRecursive(rightPos, length//2, iterations-1)

def getHeightDiff(posA, length):
    return length//2 * math.sqrt(3)

def drawOuterTriangle(length):
    # Move to topmost point
    myTurtle.up()
    myTurtle.goto(0, length//2)
    myTurtle.seth(90)
    myTurtle.down()
    # Draw downRight
    myTurtle.right(150)
    myTurtle.forward(length)
    # Draw left
    myTurtle.right(120)
    myTurtle.forward(length)
    # Draw upRight
    myTurtle.right(120)
    myTurtle.forward(length)
    myTurtle.end_fill()

def drawMidpointsTriangle(topPos, length):
    # Move to right corner of inner inverse triangle
    myTurtle.up()
    myTurtle.goto(topPos)
    myTurtle.seth(90)
    myTurtle.right(150)
    myTurtle.forward(length//2)
    # Get ready to draw
    myTurtle.down()
    myTurtle.begin_fill()
    # start going west
    myTurtle.seth(180)
    myTurtle.forward(length//2)
    # continue to bottom corner
    myTurtle.left(120)
    myTurtle.forward(length//2)
    # Cycle back to right corner
    myTurtle.left(120)
    myTurtle.forward(length//2)
    myTurtle.end_fill()

drawSierpinskiTriangle(700, 5)