#测试继承的基本使用
class person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def say_name(self):
        print(self.name)
class student(person):
    def __init__(self,name,age,sex,score):
        person.__init__(self,name,age,sex)
        self.score=score
    def say_score(self):
        print(self.socre)
s=student("小明",20,"man",100)
s.say_name()
print(s.score)