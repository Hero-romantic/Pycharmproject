# A=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# n=int(input("输入一个数0~13"))
# for x in range(n):
#    print(A[x],end='')
#    for y in range(x+1,n+x):
#        print(A[y],end='')
#    print()
A=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n=int(input())
for x in range(n):
    print(A[x],end='')
    for y in range(x+1,n+x):
        print(A[y],end='')
    print()