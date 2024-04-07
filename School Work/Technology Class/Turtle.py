import turtle as t



def goto(x:float,y:float):
    t.penup()
    t.goto(x,y)
    t.pendown()

def begin_fill(color:str):
    t.fillcolor(color)
    t.begin_fill()






def stop_sign():
    rect_length = [20, 100, 20, 100]
    circle_rad = 80

    goto(0,-circle_rad)
    begin_fill("red")
    t.circle(80, 360)
    t.end_fill()
    goto(50,-10)
    begin_fill("white")
    for length in rect_length:
        t.left(90)
        t.forward(length)
    t.end_fill()
    breakpoint()


def archery_target():
    rad = 100
    color_set = ["blue", "red", "red", "yellow", "yellow"]
    for color in color_set:
        begin_fill(color)
        goto(0,-rad)
        t.circle(rad, 360)
        rad -= 20
        t.end_fill()
    breakpoint()

def fun_shapes():
    length = 200
    while length > 0:
        t.forward(length)
        t.right(90)
        length -= 5
    breakpoint()

fun_shapes()
