print("计算数列m(n)= 1/2+2/3+...+n/(n+1)")
x=int(input("输入n的值"))
def test(x):
    if x==1:
        return 1/2
    else:
        return test(x-1)+x/(x+1)
print(test(x))