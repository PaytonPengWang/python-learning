import turtle

def main():
    size = 50

    while size <= 150:
        draw_pentagarm(size)
        size += 30
    
    turtle.exitonclick()

# 绘制五角星
def draw_pentagarm(size):
    count =0

    while count < 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1

if __name__ == '__main__':
    main()


