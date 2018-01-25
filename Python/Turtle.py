#Open Terminal. Type in Python; import turtle funtion from library
from turtle import Turtle
#assign the turtle object to a variable
jude = Turtle()
#turtle is placed on a coordinate plane. It starts at (0,0)
#move the turtle with the functions that it already knows (number of pixels)
jude.forward(100)
jude.left(90)
jude.forward(100)
jude.right(10)
jude.forward(150)

#create a tutle and draw a square

from turtle import Turtle
laura = Turtle()

laura.forward(50)
laura.left(90)
laura.forward(50)
laura.left(90)
laura.forward(50)
laura.left(90)
laura.forward(50)


#create triangle with three different colored sides. Color name is a string
from turtle import Turtle
laura = Turtle()
laura.color("pink")
laura.forward(100)
laura.left(120)
laura.color("green")
laura.forward(100)
laura.left(120)
laura.color("blue")
laura.forward(100)

#pen control
from turtle import Turtle
laura = Turtle()

laura.forward(50)

# Move 50 pixels forward with the pen up
laura.penup()
laura.forward(50)

# Move 50 pixels forward with the pen down
laura.pendown()
laura.forward(50)

laura.penup()
laura.forward(50)
laura.pendown()
laura.forward(50)
