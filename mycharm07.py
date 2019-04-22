class MyRectangle :
     def __init__(self,x=0,y=0,height=100,width=100):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
     def getArea(self):
         area= self.height * self.width
         print("面积：",area)
     def getPerimeter(self):
         C=2*(self.width+self.height)
         print("周长：",C)
     def draw(self):
         import turtle
         turtle.penup()
         turtle.goto(self.x,self.y)
         turtle.pendown()
         turtle.goto(self.x+self.width,self.y)
         turtle.goto(self.x+self.width,self.y-self.height)
         turtle.goto(self.x,self.y-self.height)
         turtle.goto(self.x,self.y)
         turtle.done()
M1= MyRectangle()
M1= MyRectangle()
M1.getArea()
M1.getPerimeter()
M1.draw()

