class Carfactory:
    object=None
    __init_flag=True
    def creatcar(self,brand):
        if brand=="奔驰":
            return Benz()
        elif brand=="宝马":
            return BMW()
        elif brand=="比亚迪":
            return BYD()
        else:
            return "品牌未知无法创建"
    def __new__(cls, *args, **kwargs):
        if cls.object==None:
            cls.object=object.__new__(cls)
        return cls.object
    def __init__(self):
        if Carfactory.__init_flag==True:
            Carfactory.__init_flag=False
            print("初始化")
class Benz:
    print("奔驰大G")
class BMW:
    print("宝马X6")
class BYD:
    print("SUV宋")
factory=Carfactory()
c1=factory.creatcar("奔驰")
c2=factory.creatcar("宝马")
c3=factory.creatcar("比亚迪")
print(c1)
print(c2)
print(c3)
factory1=Carfactory()
print(factory1)
print(factory)