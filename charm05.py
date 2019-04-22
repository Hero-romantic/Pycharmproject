import time
import math
def test1():
    start=time.time()
    for x in range(100000000):
        a=math.sqrt(2**100)
    end=time.time()
    print("耗时{0}".format(end-start))
def test2():
    start=time.time()
    b=math.sqrt
    for x in range(100000000):
        b(2**100)
    end=time.time()
    print("耗时{0}".format(end-start))
test1()
test2()


