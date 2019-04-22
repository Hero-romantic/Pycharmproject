n=int(input("给一个0~2**32d的10进制数"))
b = '{:032b}'.format(n)
c=b[::-1]
d='{:1}'.format(int(c,2))
print(b)
print(c)
print(d)