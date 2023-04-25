import turtle as t
t.penup()
t.setup(1200,1200)
t.title("Flag of Japan")
t.bgcolor("black")
t.speed(5)

flag_height=200
flag_width =flag_height*(3/2)

circle_radius=(3/5)*flag_height/2
def draw_rectangle(x,y,height, width):
    t.goto(x,y)
    t.pendown()
    t.fillcolor("white")
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

def draw_circle(x,y,radius,color):
    t.penup()
    t.goto(x,y)
    t.color("red")
    t.fillcolor(color)
    t.begin_fill()
    t.pendown()
    t.right(90)
    t.circle(radius)
    t.end_fill()
    t.penup()


draw_rectangle(0,0,flag_height,flag_width)
draw_circle(150,-160,circle_radius, 'red')

t.hideturtle()
t.done()

