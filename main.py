# Create the window first
# create the box before the border to prevent overlapping
# create the text on top of the boxshelf
# make the border of the bookshelf
# move stacey and make a loop to get all the text inside the box
# finish

from turtle import *

window = Screen()
window.bgcolor("#FFE5C5")

penup()
setposition(-250, 250)
pensize(5)
forward(25)
pendown()

color("#A2542E")
begin_fill()
right(90)
forward(500)
left(90)
forward(450)
left(90)
forward(500)
left(90)
end_fill()

penup()
setposition(-150, 300)
write("Tracey's Book Shelf", font=("Arial", 25))
setposition(-250, 250)

setheading(360)

color("#A72D29")
pendown()
pensize(30)
forward(500)
penup()
setposition(-250, -250)
pendown()
pensize(30)
forward(500)
penup()

setposition(0, 0)


window.exitonclick()