# lab01_turtle.py

import turtle

# right arm
turtle.setposition(0, 0)
turtle.left(45)
turtle.forward(35)

# left arm
turtle.penup()
turtle.setposition(0, 0)
turtle.pendown()
turtle.left(90)
turtle.forward(35)

# body
turtle.penup()
turtle.setposition(0, 35)
turtle.pendown()
turtle.left(135)
turtle.forward(70)

# right leg
turtle.left(45)
turtle.forward(45)
turtle.penup()

# left leg
turtle.setposition(0, -35)
turtle.pendown()
turtle.right(90)
turtle.forward(45)

# left eye
turtle.fillcolor('green')
turtle.begin_fill()
turtle.penup()
turtle.setposition(-14, 70)
turtle.pendown()
turtle.circle(5)
turtle.end_fill()

# right eye
turtle.fillcolor('green')
turtle.begin_fill()
turtle.penup()
turtle.setposition(8, 70)
turtle.pendown()
turtle.circle(5)
turtle.end_fill()

# mouth
turtle.penup()
turtle.setposition(-6, 45)
turtle.left(135)
turtle.pendown()
turtle.forward(20)

# head
turtle.penup()
turtle.setposition(0, 35)
turtle.pendown()
turtle.circle(25)

# nose
turtle.penup()
turtle.setposition(-5, 52)
turtle.right(145)

turtle.done()
