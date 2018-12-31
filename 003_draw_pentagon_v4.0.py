"""
    绘制分行树
    0. 绘制主干
    1. 绘制右侧树枝
    2. 返回树枝节点
    3. 绘制左侧树枝
    4. 返回树枝节点
"""

import turtle

INIT_LENGTH = 80
MIN_LENGTH = 20
STEP = 10

def main():
    init_config()
    turtle.left(90)
    turtle.forward(INIT_LENGTH+STEP)
    drawing(INIT_LENGTH)
    
    turtle.exitonclick()

def drawing(length):
    if length - STEP < MIN_LENGTH:
        turtle.pencolor('green')
    print(length)
    turtle.right(20)

    forward(length)
    if length > MIN_LENGTH:
        drawing(length - STEP)
    back(length)
    print(length)
    turtle.left(40)
    forward(length)
    if length > MIN_LENGTH:
        drawing(length - STEP)
    back(length)
    turtle.right(20)

    turtle.pencolor("brown");

def forward_and_back(length):
    forward(length)
    back(length)

def forward(length):
    turtle.forward(length)
    
def back(length):
    turtle.penup()
    turtle.backward(length)
    turtle.pendown()

def init_config():
    turtle.penup()
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('brown');

if __name__ == '__main__':
    main()


