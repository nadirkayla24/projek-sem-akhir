import turtle

li = turtle.Turtle()
li.screen.bgcolor("black")
li.pensize(2)
li.color("blue")
li.left(90)
li.backward(60)
li.speed(50000)
li.shape("turtle")

def love(i):
    if i<10:
        return
    else:
        li.forward(i)
        li.color("red")
        li.circle(2)
        li.color("blue")
        li.left(30)

        love(3*i/4)

        li.right(60)

        love(3*i/4)

        li.left(30)
        li.backward(i)
love(60)
turtle.done()