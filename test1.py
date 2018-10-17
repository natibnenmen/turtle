import turtle               # allows us to use the turtles library
from itertools import repeat
#wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()      # create a turtle named alex
turtle.title(__file__)
#alex.speed("fastest")
#for i in range(4):
for i in repeat(None, 4):
    alex.forward(150)           # tell alex to move forward by 150 units
    alex.left(90)               # turn by 90 degrees
#alex.forward(75)     
print "Press any key to exit..."
name = raw_input()
