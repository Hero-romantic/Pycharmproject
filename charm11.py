#定义一个函数实现反响输出一个整数。比如：输入 3245，输出 5432
while 1:
   x=input("输入一个数字")
   if type (eval(x)) is int:
    print("请重新输入一个整数")
    break
   else:
       print("请重新输入一个整数")
       continue
def test():
      print(x[::-1])
test()
