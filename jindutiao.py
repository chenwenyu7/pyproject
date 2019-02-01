import time
scale = 10
print("{0:=^20}".format("执行开始"))
for i in range(scale + 1):
    a = i * '*'
    b = '.' * (scale-i)
    c = (i / scale) * 100
    time.sleep(0.9)
    print("{:^3.0f}% [{}>{}]".format(c,a,b),end = "\r")
print("{:=^20}".format("执行结束"))
    
