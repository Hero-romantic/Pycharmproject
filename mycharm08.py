#测试类方法，静态方法
class school:
    university="cqupt"
    @classmethod
    def printUniversity(cls):
        print(cls.university)
school.printUniversity()
class human:
    man="小明"
    @staticmethod
    def add(a,b):
        print("{0}+{1}={2}".format(a,b,(a+b)))
        return a+b
human.add(10,10)