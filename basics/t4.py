from turtle import *
side  = 5
size = 90
pensize(8)
for i in range(side):
    pencolor('black')
    forward(size)
    for i in range(3):
        pencolor('blue')
        forward(25)
        left(90)
    left(360/5)
mainloop()