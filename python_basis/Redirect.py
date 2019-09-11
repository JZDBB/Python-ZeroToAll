"""
输出重定向
默认情况下，print 函数会将内容打印输出到标准输出流(即 sys.stdout)，可以通过 file 参数自定义输出流。

也可以输出到错误输出流，例如：
"""

import sys

# Method 1
with open('data.log', 'w') as fileObj:
    print('hello world!', file=fileObj)
print('hello world!', file=sys.stderr)

# Method 2
f=open('print.txt','a+')
old=sys.stdout #将当前系统输出储存到临时变量
sys.stdout=f   #输出重定向到文件
print('Hello World!') #测试一个打印输出
sys.stdout=old     #还原系统输出

# Method 3
year=1
years=15
bj=10000
rate=0.05
f=open('total.txt','w+')
while year < years:
	bj=bj*(1+rate)
	print("第%d年，本息合计%0.2f" % (year,bj), file=f)
	year+=1


# Method 4
class FakeOut:
    def __init__(self):
        self.str=''
        self.n=0
    def write(self,s):
        self.str+="Out:[%s] %s\n"%(self.n,s)
        self.n+=1
    def show(self): #显示函数，非必须
        print(self.str)
    def clear(self): #清空函数，非必须
        self.str=''
        self.n=0
f=FakeOut()
import sys
old=sys.stdout
sys.stdout=f
print('Hello weord.')
print('Hello weird too.')
sys.stdout=old
f.show()
