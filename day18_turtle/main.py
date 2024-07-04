from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
screen = Screen()
tim.shape("turtle")
# tim.color("red")
tim.speed(7)
colormode(255)
# tim.pensize(10)

# # square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# # dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()

# # different shapes
# for side in range(4, 9):
#     angle = 360 // side
#     r = random.randint(1, 255)
#     g = random.randint(1, 255)
#     b = random.randint(1, 255)
#     tim.color((r, g, b))
#     for _ in range(side):
#         tim.forward(100)
#         tim.right(angle)

# # random walk
# for _ in range(100):
#     r = random.randint(1, 255)
#     g = random.randint(1, 255)
#     b = random.randint(1, 255)
#     tim.color((r, g, b))
#
#     luck = random.randint(1, 4)
#
#     if luck == 1:
#         tim.right(180)
#     elif luck == 2:
#         tim.right(90)
#     elif luck == 3:
#         tim.left(90)
#     tim.forward(20)

# spirograph
angle = 20
for _ in range(360//angle):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tim.color((r, g, b))
    tim.circle(100)
    tim.right(angle)

screen.exitonclick()
