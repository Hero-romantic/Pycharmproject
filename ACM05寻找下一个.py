#1~4是为了能一行能输入多个值
n=int(input("要输入的数字个数："))
list1=[]
list2=[]
list2=input().split()
list=[]
#8~9 将list2字符串类型的元素，转化为int类型元素构成的列表list1
for x in range(n):
    list1.append(int(list2[x]))
#11~12 循环依次抽出list1列表中的元素
for i in range(len(list1)):
    a=list1[i]
#13 为什么i+1？先抽出第i+1个元素。由题意由1开始计算，而rang()函数从0开始
    for j in range(i+2,len(list1)+1):
        if a<list1[j-1]:
            list.append(j)
            break
        else:
            if j<len(list1):
               pass
            else:
                list.append(-1)
list.append(-1)
print(list)
