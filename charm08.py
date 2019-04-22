#输入三角形三个顶点的坐标，若有效则计算三角形的面积；如坐标无效，则给出提示
import math
print("请输入第一个点坐标")
x1=float(input("输入x1坐标"))
y1=float(input("输入Y1坐标"))
print("请输入第二个点坐标")
x2=float(input("输入x2坐标"))
y2=float(input("输入Y2坐标"))
print("请输入第三个点坐标")
while 1:
  x3=float(input("输入x3坐标"))
  y3=float(input("输入Y3坐标"))
  a=[(x1,y1),(x2,y2),(x3,y3)]
  if (y3-y2)/(x3-x2)==(y2-y1)/(x2-x1):
      print("输入的三个坐标在同一直线，请重新输入第三个点坐标")
      continue
  else:
      a=math.sqrt((x3-x2)**2+(y3-y2)**2)
      b=math.sqrt((x2-x1)**2+(y2-y1)**2)
      c=math.sqrt((x1-x3)**2+(y1-y3)**2)
      p=(a+b+c)/2
      print("三角形面积：",math.sqrt(p*(p-a)*(p-b)*(p-c)))#利用海伦公式
      break