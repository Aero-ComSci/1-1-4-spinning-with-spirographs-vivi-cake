import turtle as trtl 


screen = trtl.Screen()
screen.setup(800, 800)

pen = trtl.Turtle()

pen.speed(10)

num = 5
size = 700
move = 30

length = -size/2
height = size/2

pen.up()
pen.goto(length, height)
pen.down()

for i in range(12):
    if i % 2 == 0:
        pen.color("black")
    else:
        pen.color("thistle")

    pen.begin_fill()
    for i in range(4):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()
 

    length += move
    height -= move
    pen.up()
    pen.goto(length, height)
    pen.down()
    size -= 60
    pen.setheading(0)

screen.mainloop()
