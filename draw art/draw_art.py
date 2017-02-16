import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forword(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle Brad - Drwas a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(1,5):
        draw_square(brad)
        brad.right(10)
    #Create the turtle Angle - Draws a circle
    #angle = turtle.Turtle()
    #angle.shape("arrow")
    #angle.color("blue")
    #angle.circle(100)

    window.exitonclick()

draw_art()
