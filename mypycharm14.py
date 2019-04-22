#工厂设计模式
class cqupt:
    def university(self,college):
        if college=="软件工程学院":
            return software()
        elif college=="计算机学院":
            return  computer()
        elif college=="传媒艺术学院":
            return art()
        else :
            print("未知学院无法创建")
class software:
      pass
class computer:
    pass
class art:
    pass
school=cqupt()
s1=school.university("软件工程学院")
s2=school.university("计算机学院")
s3=school.university("传媒艺术学院")
print(s1)
print(s2)
print(s3)
