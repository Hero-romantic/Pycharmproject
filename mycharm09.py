#析构方法
class Person:
    def __del__(self):
        print("销毁对象{0}".format(self))
P1=Person()
P2=Person()
print(P1)
print(P2)
del(P2)
print("*********")
print(P1)
print(P2)