import turtle as t
t.setup(1200,1200)
t.title("Flag of America")

flag_height=250
flag_width=flag_height*1.9 #475

canton_height=flag_height*(7/13)
canton_width=flag_width*(2/5)

strips_height=flag_height/13
strips_width=flag_width

x1=0
y1=0


def draw_rectangle(x1,y1,height, width, color):
    t.goto(x1,y1)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.end_fill()
    t.penup()



def draw_stripes():
    x = x1
    y = y1
    for strips in range(0,6):
        for color in ["red", "white"]:
            draw_rectangle(x,y,strips_height, strips_width, color)
            y=y-strips_height

    draw_rectangle(x,y,strips_height, strips_width, "red")
    y=y-strips_height


stars_size=4.3
stars_col_space= 0.0633*flag_height
stars_row_space= 0.0538*flag_height


t.speed(20)
def star_shape(x,y,width):
    t.goto(x,y)
    t.begin_fill()
    t.fillcolor("white")
    for i in range(5):
        t.right(144)
        t.forward(width)
        t.left(72)
        t.forward(width)
    t.end_fill()


def six_stars():

    #dis_of_stars=stars_col_space*2
    #verticl_dis_of_stars=stars_row_space*2
    y= -10.5 #0.0538*250 13.45
    for row in range(0,5):
        x=20 #15.825
        for stars in range(0,6):
            star_shape(x,y,stars_size)
            x=x+stars_col_space*2
        y=y-stars_row_space*2


def five_stars():
    y = -23 # 0.0538*250 13.45
    for row in range(0, 4):
        x = 36  # 15.825
        for stars in range(0, 5):
            star_shape(x, y, stars_size)
            x = x + stars_col_space * 2
        y = y - stars_row_space * 2


draw_stripes()
draw_rectangle(x1,y1,canton_height, canton_width, 'navy')
six_stars()
five_stars()
t.done()

