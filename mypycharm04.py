import turtle
for x in range(1,11):
    turtle.speed(0.5)
    turtle.width(5)
    a=["red","green","yellow","black","red","green","yellow","black","red","green"]
    turtle.color(a[x-1])
    turtle.penup()
    turtle.goto(0,-25*x)
    turtle.pendown()
    turtle.circle(25*x)


