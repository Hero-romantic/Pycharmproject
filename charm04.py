a=[20,30]
print(a)
print(id(a))
def test1(m):
    a.append(m)
    print(m)
test1(10)
print(a)
print(id(a))

