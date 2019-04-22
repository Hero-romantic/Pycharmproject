# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.patches import Circle
# # 投点次数
# n = 10000
# # 圆的半径、圆心
# r = 1.0
# a,b = (0.,0.)
# # 正方形区域
# x_min, x_max = a-r, a+r
# y_min, y_max = b-r, b+r
# # 在正方形区域内随机投点
# x = np.random.uniform(x_min, x_max, n)
# #均匀分布
# y = np.random.uniform(y_min, y_max, n)
# #计算点到圆心的距离
# d = np.sqrt((x-a)**2 + (y-b)**2)
# #统计落在圆内点的数目
# res = sum(np.where(d < r, 1, 0))
# #计算pi的近似值（Monte Carlo:用统计值去近似真实值）
# pi = 4 * res / n
# print('pi: ',pi)
# #画个图
# fig = plt.figure()
# axes = fig.add_subplot(111)
# axes.plot(x, y,'ro',markersize = 1)
# plt.axis('equal')
# #防止图像变形
# circle = Circle(xy=(a,b), radius=r ,alpha=0.5)
# axes.add_patch(circle)
# plt.show()


import random
from fractions import gcd
s=[]
s=input("分别输入a,b,n").split()
r=[]
for x in range(len(s)):
   r.append(int(s[x]))
a=r[0]
b=r[1]
n=r[2]
count=0
# x_min,x_max=-a,a
# y_min,y_max=-b,b
for i in range(n):
    D = []
    d = []
    D=input("分别输入 X"+str(x)+" Y"+str(x)+" 坐标").split()
    for j in range(2):
        d.append(int(D[j]))
    x=d[0]
    y=d[1]
    if x**2/a**2+y**2/b**2<=1:
        count=count+1
S=4*a*b*(count/n)
if isinstance(S,int):
    print("面积:",str(S))
else:
    m=gcd(4*a*b*count,n)
    print("面积:",4*a*b*count/m,"/",n/m)


# import random
# from fractions import gcd
# s=[]
# s=input().split()
# r=[]
# for x in range(len(s)):
#    r.append(int(s[x]))
# a=r[0]
# b=r[1]
# n=r[2]
# count=0
# for i in range(n):
#     D = []
#     d = []
#     D=input().split()
#     for j in range(2):
#         d.append(int(D[j]))
#     x=d[0]
#     y=d[1]
#     if x**2/a**2+y**2/b**2<=1:
#         count=count+1
# S=4*a*b*(count/n)
# if isinstance(S,int):
#     print(str(S))
# else:
#     m=gcd(4*a*b*count,n)
#     print(4*a*b*count/m,"/",n/m)