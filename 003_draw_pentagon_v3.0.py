"""
    递归函数
"""

import turtle

def main():
    turtle.penup();
    turtle.backward(200);
    turtle.pendown();
    turtle.pensize(2);
    turtle.pencolor("#3ff");

    size = 50

    draw_pentagarms(size)

    
    turtle.exitonclick()

# 递归绘制五角星
def draw_pentagarms(size):
    if size <= 150:
        draw_pentagarm(size,0)
        size += 30
        draw_pentagarms(size);

# 绘制五角星
def draw_pentagarm(size,count):
    
    turtle.forward(size)
    turtle.right(144)

    count += 1
    if count < 5:
        draw_pentagarm(size,count)

if __name__ == '__main__':
    main()


