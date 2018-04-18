from fractions import Fraction #导入分数函数
import numpy as np
import cProfile
# def size():
print("你需要算的是分数还是整数？")
a=input()
if a=="分数":
    x = np.random.randint(1,100)
    y = np.random.randint(1,100)
    e = input("加减乘除？")
    b = np.random.randint(1,100)
    c = np.random.randint(1,100)
    print(x,y,b,c)
    if e=="+":
        print("答案为:%s+%s=%s"%(Fraction(x,y),Fraction(b,c),Fraction(x, y) + Fraction(b, c)))
    elif e=="-":
        print("答案为:%s-%s=%s" % (Fraction(x, y), Fraction(b, c), Fraction(x, y) - Fraction(b, c)))
    elif e=="*":
        print("答案为:%s*%s=%s" % (Fraction(x, y), Fraction(b, c), Fraction(x, y) * Fraction(b, c)))
    elif e=="/":
        print("答案为:%s/%s=%s" % (Fraction(x, y), Fraction(b, c), Fraction(x, y) / Fraction(b, c)))
elif a=="整数":
    x1=np.random.randint(1,100)
    y1=np.random.randint(1,100)
    print(x1,y1)
    e1=input("加减乘除？")
    if e1 == "+":
        print("答案为:%s+%s=%s" %(x1, y1, x1+y1))
    elif e1== "-":
        print("答案为:%s-%s=%s" %(x1, y1, x1-y1))
    elif e1 == "*":
        print("答案为:%s*%s=%s" %(x1, y1, x1 * y1))
    elif e1=="/":
        print("答案为:%s/%s=%s" %(x1, y1, x1 / y1))
# cProfile.run(size)