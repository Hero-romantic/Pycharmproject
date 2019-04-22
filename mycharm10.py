#测试可调用方法__call__()
class salaryall:
    def __call__(self,salary):
        daysalary=salary//30
        hoursalary=daysalary//24
        yearsalary=salary*12
        return dict(yearsalary=yearsalary,mothsalary=salary,daysalary=daysalary,hoursalary=hoursalary)
S1=salaryall()
print(S1(3000))

