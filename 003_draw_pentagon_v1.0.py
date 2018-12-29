import turtle

def main():
    step = 150
    while step > 10:
        count = 0
        while count < 5:
            turtle.forward(step)
            turtle.right(144)
            count = count + 1
        turtle.forward(step-10)
        step = step - 10
        turtle.right(144)
    
    
    turtle.exitonclick()

if __name__ == '__main__':
    main()


