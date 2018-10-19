# TODO: Create maze methods, and then progran turtle to explore it
# Basic movement procedure
# From our starting position we will first try going North one square and then recursively try our procedure from there.
# If we are not successful by trying a Northern path as the first step then we will take a step to the South and recursively repeat our procedure.
# If South does not work then we will try a step to the West as our first step and recursively apply our procedure.
# If North, South, and West have not been successful then apply the procedure recursively from a position one step to our East.
# If none of these directions works then there is no way to get out of the maze and we fail.

# Drop 'breadcrumbs' to signify locations we've visited and ignore those locations

# Four base cases
# The turtle has run into a wall. Since the square is occupied by a wall no further exploration can take place.
# The turtle has found a square that has already been explored. We do not want to continue exploring from this position or we will get into a loop.
# We have found an outside edge, not occupied by a wall. In other words we have found an exit from the maze.
# We have explored a square unsuccessfully in all four directions.

# Maze representation methods
# __init__ Reads in a data file representing a maze, initializes the internal representation of the maze, and finds the starting position for the turtle.
# drawMaze Draws the maze in a window on the screen.
# updatePosition Updates the internal representation of the maze and changes the position of the turtle in the window.
# isExit Checks to see if the current position is an exit from the maze.
# The Maze class also overloads the index operator [] so that our algorithm can easily access the status of any particular square.
#     This file is a text file that represents a maze by using “+” characters for walls, spaces for open squares, and the letter “S” to indicate the starting position

# Turtle wil explore the maze using this method
# def searchFrom(maze, startRow, startColumn):



