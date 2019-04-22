import turtle
for x in range(1,18):
          turtle.goto(180,(x-1)*10)
          turtle.penup()
          turtle.goto(0,(x-1)*10+10)
          turtle.pendown()
          turtle.goto(180,x*(10))
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
for i in range(1,19):
          turtle.goto((i-1)*10,0)
          turtle.goto((i-1)*10,180)
          turtle.goto((i)*10,180)
          turtle.goto((i)*10,0)
turtle.done()


