#员工一共 4 人。录入这 4 位员工的薪资。全部录入后，打印提示“您已经全部录入 4名员工的薪资”。最后，打印输出录入的薪资和平均薪资
print("请录入四个员工的工资")
salary=[]
t_salary=0
for x in range(4):
    s=input("依次输入4名员工的工资")
    t_salary+=float(s)
    salary.append(float(s))
print("您已经全部录入 4名员工的薪资")
print("录入的薪资{0}".format(salary))
print("四名员工的平均薪酬为",t_salary/4)