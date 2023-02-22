import turtle
t = turtle.Pen()
t.shape('turtle')
for i in range(20):
    t.pencolor('orange')
    t.forward(i*20)
    t.right(135)
    t.circle(i*10)
    t.left(20)
