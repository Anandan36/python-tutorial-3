import turtle

hex = turtle.Turtle()
hex.speed(0)

for _ in range(10):
    for _ in range(6):
        hex.forward(50)
        hex.left(60)
    hex.right(36)

turtle.done()
