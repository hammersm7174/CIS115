# CIS115
# hammersm
# M3T2
# 10/3/18

# Turtle Python example 2

import turtle

def main():
        
    sides = int(input('Number of sides? '))
    size = int(input('Size of polygon? '))
    
    win = turtle.Screen()
    alex = turtle.Turtle()
    bob = turtle.Turtle()
    christine = turtle.Turtle()

    # space the turtles apart
    alex.backward(size*2)
    bob.forward(0)
    christine.forward(size*2)
    
    # customize the turtles
    alex.pensize(3)
    bob.pensize(4)
    christine.pensize(2)
    alex.pencolor('red')
    bob.pencolor('green')
    christine.pencolor('blue')
    


    # draw shapes
    for t in [alex, bob, christine]:
        drawPolygon(t, sides, size)
        

def drawPolygon(t, sides, size):
    '''
    uses turtle to draw a n sided polygon.
    input: t - a turtle
            sides - number of sides
            size - length of one side
    '''
    for side in range(sides):
        t.forward(size)
        t.right(360/sides) # angle depends on polygon

# run program
main()
