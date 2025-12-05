from turtle import Turtle,Screen
import random

#create screen object and set width and height
screen = Screen()
screen.setup(800,500)

#make sure still race is not start
is_race_on = False

#take user bet as input
user_bet = screen.textinput(title="make your bet..",prompt="which turtle will win the race? enter a color"
                                                           "(red/orange/yellow/green/blue/indigo/purple) : ")

#lists for store turtle objects, colors, and starting coordinates of the turtles
new_turtle =[]
colors=["red","orange","yellow","green","blue","indigo","purple"]
starting_y_coordinate = [-210,-140,-70,0,70,140,210]


#this for loop use to create turtle objects and store them inside the 'new_turtle' list
for i in range(0,7):
    turtle = Turtle()
    turtle.color(colors[i])
    turtle.shape("turtle")
    turtle.shapesize(2,2)
    turtle.penup()
    turtle.goto(-370,starting_y_coordinate[i])
    new_turtle.append(turtle)


#after user enter a color, start the race
if user_bet:
    is_race_on= True


#while loop use to repeat the turtles motion until one turtle won
#for loop use to give random forward distances for each turtle
#if condition check which turtle won and print the result on the window
while is_race_on:
    for turtle in new_turtle:
        if turtle.xcor()>380:
            winning_color =turtle.pencolor()
            if user_bet == winning_color:
                turtle.stamp()
                turtle.hideturtle()
                turtle.goto(-80,0)
                turtle.write(f"you won!!!..the {winning_color} turtle is the winner.",align="center",
                             font=("Arial", 20, "normal"))
            else:
                turtle.stamp()
                turtle.hideturtle()
                turtle.goto(-80,0)
                turtle.write(f"you lost!!!..the {winning_color} turtle is the winner.", align="center",
                             font=("Arial", 20, "normal"))
            is_race_on=False
            break
        distance = random.randint(0,10)
        turtle.forward(distance)


# to exit the turtle graphics window by click...otherwise it automatically disappear
screen.exitonclick()