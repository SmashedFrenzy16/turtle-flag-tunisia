from turtle import *
bgcolor("red")
up()
goto(0,-90)
down()
color("white")
begin_fill()
circle(90)
end_fill()

up()
goto(0,-60)
down()
color("red")
begin_fill()
circle(60)
end_fill()

up()
goto(18,-54)
down()
color("white")
begin_fill()
circle(54)
end_fill()

up()
goto(0,-10)
down()

AF=25
a=180-180/5
color("red")
begin_fill()
for i in range(5):
    forward(AF)
    right(a-360/5)
    forward(AF)
    left(a)
end_fill()

hideturtle()
