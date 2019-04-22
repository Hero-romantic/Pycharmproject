#测试浅拷贝和深拷贝
import copy
#测试浅拷贝
def test1():
  a=[10,20,[30,40]]
  b=copy.copy(a)
  print(a)
  print(b)
  #修改b后
  b.append(50)
  b[2].append(35)
  print(a)
  print(b)
  print("*"*20)
#测试深拷贝
def test2():
  c=[10,20,[30,40]]
  d=copy.deepcopy(c)
  print(c)
  print(d)
  #修改b后
  d.append(50)
  d[2].append(35)
  print(c)
  print(d)
test1()
test2()