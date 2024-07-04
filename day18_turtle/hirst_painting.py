# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen, colormode
import random

color_list = [(253, 251, 248), (254, 250, 252), (231, 251, 242), (198, 12, 32), (250, 237, 17), (39, 77, 189),
              (38, 217, 67), (238, 228, 5), (229, 159, 46), (27, 39, 158)]

tim = Turtle()
screen = Screen()
colormode(255)
# tim.pensize(10)
tim.penup()

for k in range(10):
    tim.goto(-250, k * 50)
    for _ in range(10):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.forward(50)

screen.exitonclick()
