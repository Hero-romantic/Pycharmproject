#海龟画循环图
import turtle
import math
a=800
r=400
turtle.speed(20)
for x in range(10):
  turtle.penup()
  turtle.goto(-a/2,-a/2)
  turtle.pendown()
  turtle.goto(a/2,-a/2)
  turtle.goto(a/2,a/2)
  turtle.goto(-a/2,a/2)
  turtle.goto(-a/2,-a/2)
  turtle.penup()
  turtle.goto(0,-r)
  turtle.pendown()
  turtle.circle(r)
  a=math.sqrt((r**2))*math.sqrt(2)
  r=a/2
a = 800
r = 400
turtle.penup()
turtle.goto(-a/2,-a/2)
turtle.pendown()
turtle.goto(a/2,a/2)
turtle.penup()
turtle.goto(-a/2,a/2)
turtle.pendown()
turtle.goto(a/2,-a/2)
turtle.penup()
turtle.goto(a/2,0)
turtle.pendown()
turtle.goto(-a/2,0)
turtle.penup()
turtle.goto(0,a/2)
turtle.pendown()
turtle.goto(0,-a/2)

turtle.done()


