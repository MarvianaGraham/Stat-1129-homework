import turtle as t
import math
t.setup(1200,1200)
t.title("Flag of China")
flag_height=200
flag_width=300

def draw_rectangle(x,y,height,width,color1, color2):
    t.color(color1)
    t.fillcolor(color2)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.end_fill()
    t.penup()

t.speed(20)

def draw_star(x,y,width,color,angle):
    t.goto(x,y)
    t.right(angle)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    for i in range(5):
        t.right(144)
        t.forward(width)
        t.left(72)
        t.forward(width)
    t.end_fill()
    t.penup()

big_star_size= 15
small_star_size=7

draw_rectangle(0,0,200,300,"red","red")

draw_star(50,-25, big_star_size, "yellow",18)
draw_star(100,-10,small_star_size,"yellow", 15)
draw_star(120,-40,small_star_size,"yellow", 30)
draw_star(120,-70,small_star_size,"yellow", 24)
draw_star(105,-100,small_star_size,"yellow", 30)
t.hideturtle()
t.done()