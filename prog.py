# import the turtle module
import turtle

# define some constant values for colors and shadows
BODY_COLOR = 'red'
BODY_SHADOW = ''
GLASS_COLOR = 'grey'
GLASS_SHADOW = ''

# get a reference to the turtle screen and create a turtle object
s = turtle.getscreen()
tur = turtle.Turtle()

# set the speed of the turtle to 10
tur.speed(100)

# define a function to draw the body of the robot
def body():
    # set the pen size and fill color
    tur.pensize(20)
    tur.fillcolor(BODY_COLOR)
    tur.begin_fill()

    # draw the main body of the robot
    tur.right(90)
    tur.forward(50)
    tur.right(180)
    tur.circle(40, -180)
    tur.right(180)
    tur.forward(200)
    tur.right(180)
    tur.circle(100, -180)
    tur.backward(20)
    tur.left(15)
    tur.circle(500, -20)
    tur.backward(20)
    tur.circle(40, -180)
    tur.left(7)
    tur.backward(50)

    # draw the robot's head
    tur.up()
    tur.left(90)
    tur.forward(10)
    tur.right(90)
    tur.down()
    tur.right(240)
    tur.circle(50, -70)

    # finish filling the body
    tur.end_fill()

# define a function to draw the robot's glass
def glass():
    # move the turtle to the appropriate location
    tur.up()
    tur.right(230)
    tur.forward(100)
    tur.left(90)
    tur.forward(20)
    tur.right(90)
    tur.down()

    # set the fill color and begin filling
    tur.fillcolor(GLASS_COLOR)
    tur.begin_fill()

    # draw the glass
    tur.right(150)
    tur.circle(90, -55)
    tur.right(180)
    tur.forward(1)
    tur.right(180)
    tur.circle(10, -65)
    tur.right(180)
    tur.forward(110)
    tur.right(180)
    tur.circle(50, -190)
    tur.right(170)
    tur.forward(80)
    tur.right(180)
    tur.circle(45, -30)

    # finish filling the glass
    tur.end_fill()

# define a function to draw the robot's backpack
def backpack():
    # move the turtle to the appropriate location
    tur.up()
    tur.right(60)
    tur.forward(100)
    tur.right(90)
    tur.forward(75)

    # set the fill color and begin filling
    tur.fillcolor(BODY_COLOR)
    tur.begin_fill()

    # draw the backpack
    tur.down()
    tur.forward(30)
    tur.right(255)
    tur.circle(300, -30)
    tur.right(260)
    tur.forward(30)

    # finish filling the backpack
    tur.end_fill()

# call the three functions to draw the robot's body, glass, and backpack
body()
glass()
backpack()

# tell the screen to stay open until the user clicks on it
tur.screen.exitonclick()