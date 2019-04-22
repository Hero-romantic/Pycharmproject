#计算N阶乘
def math(n):
    if n==1:
        return 1
    else:
        return n*math(n-1)
n=int(input("输入数字"))
result=math(n)
print(n,"!=",result)


