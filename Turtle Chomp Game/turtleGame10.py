
# Turtle Graphics Game – Space Turtle Chomp

import turtle
import math
import random
import os
import time


# Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('black')
wn.bgpic('turtleGame-bg.gif')
wn.tracer(3)

# Draw border
mypen = turtle.Turtle()
mypen.color("darkorchid")
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.speed(0)
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color('darkorchid')
player.shape('turtle')
player.penup()
player.speed(0)

# Create opponent turtle
comp = turtle.Turtle()
comp.color('gold')
comp.shape('turtle')
comp.penup()
comp.setposition(random.randint(-290, 290), random.randint(-290, 290))


# Create competition score
mypen2 = turtle.Turtle()
mypen2.color('gold')
mypen2.hideturtle()

# Create variable score
score = 0
comp_score=0

# Create food
maxFoods = 10
foods = []

for count in range(maxFoods):
    foods.append (turtle.Turtle())
    foods[count].color("lightgreen")
    foods[count].shape("circle")
    foods[count].shapesize(.5)
    foods[count].penup()
    foods[count].speed(0)
    foods[count].setposition(random.randint(-290, 290), random.randint(-290, 290))

# Set speed variable
speed = 1

# Set game time limit for 1 minute (60 seconds)
timeout = time.time() + 10*6

# Define functions

def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increasespeed():
    global speed
    speed += 1

def isCollision(t1, t2):
       d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
       if d < 20:
           return True
       else:
           return False


# Set keyboard binding
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increasespeed, 'Up')



while True:
    gametime = 0
    if gametime == 6 or time.time() > timeout:
        break
    gametime = gametime - 1

    player.forward(speed)
    comp.forward(10)

    # Boundary Comp Checking x coordinate
    if comp.xcor() > 290 or comp.xcor() < -290:
        comp.right(75)
        os.system('afplay bounce.mp3&')

    # Boundary Comp Checking y coordinate
    if comp.ycor() > 290 or comp.ycor() < -290:
        comp.right(75)
        os.system('afplay bounce.mp3&')

    # Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(125)
        os.system('afplay bounce.mp3&')

    # Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(125)
        os.system('afplay bounce.mp3&')

    # Move food around
    for food in foods:
        food.forward(3)
    
        # Boundary Food Checking x coordinate
        if food.xcor() > 290 or food.xcor() < -290:
            food.right(150)
            os.system('afplay bounce.mp3&')

        # Boundary Food Checking y coordinate
        if food.ycor() > 290 or food.ycor() < -290:
            food.right(150)
            os.system('afplay bounce.mp3&')

        # Collision checking
        if isCollision(player, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0, 360))
            os.system('afplay chomp.mp3&')
            score +=1

        # Comp Collision checking
        if isCollision(comp, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0,360))
            os.system('afplay bounce.mp3&')
            comp_score+=1

        # Draw the Comp score on the screen
            mypen2.undo()
            mypen2.penup()
            mypen2.hideturtle()
            mypen2.setposition(200, 305)
            scorestring ="Score: %s" % comp_score
            mypen2.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

            # Draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring ="Score: %s" % score
            mypen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

if (int(score) > int(comp_score)):
    mypen.setposition(0, 0)
    mypen.color("darkorchid")
    mypen.write("Game Over: You WIN", False, align="center", font=("Arial", 28, "normal"))
else:
    mypen.setposition(0, 0)
    mypen.color("gold")
    mypen.write("Game Over: You LOOSE", False, align="center", font=("Arial", 28, "normal"))
    
delay = input("Press Enter to finish.")