# python normal tips
# 交换赋值
a = 2
b = 3
a, b = b, a

# Unpacking 
l = ['David', 'Pythonista', '+1-514-555-1234']
first_name, last_name, phone_number = l
# Python 3 Only
first, *middle, last = another_list

# in Operation
##不推荐
if fruit == "apple" or fruit == "orange" or fruit == "berry":
    # 多次判断  
##推荐
if fruit in ["apple", "orange", "berry"]:
    # 使用 in 更加简洁

# str Operation
##不推荐
colors = ['red', 'blue', 'green', 'yellow']

result = ''
for s in colors:
    result += s  #  每次赋值都丢弃以前的字符串对象, 生成一个新对象  
##推荐
colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)  #  没有额外的内存分配

# dict Operation
##不推荐
for key in my_dict.keys():
    #  my_dict[key] ...  
##推荐
for key in my_dict:
    #  my_dict[key] ...
# 只有当循环中需要更改key值的情况下，我们需要使用 my_dict.keys()
# 生成静态的键值列表。

##不推荐
if my_dict.has_key(key):
    # ...do something with d[key]  

##推荐
if key in my_dict:
    # ...do something with d[key]

# get setdefault
##不推荐
navs = {}
for (portfolio, equity, position) in data:
    if portfolio not in navs:
            navs[portfolio] = 0
    navs[portfolio] += position * prices[equity]
##推荐
navs = {}
for (portfolio, equity, position) in data:
    # 使用 get 方法
    navs[portfolio] = navs.get(portfolio, 0) + position * prices[equity]
    # 或者使用 setdefault 方法
    navs.setdefault(portfolio, 0)
    navs[portfolio] += position * prices[equity]

# 判断真伪
if x:
	return

# 遍历索引
##不推荐
items = 'zero one two three'.split()
# method 1
i = 0
for item in items:
    print i, item
    i += 1
# method 2
for i in range(len(items)):
    print i, items[i]

##推荐
items = 'zero one two three'.split()
for i, item in enumerate(items):
    print i, item

# 列表推导
##不推荐
new_list = []
for item in a_list:
    if condition(item):
        new_list.append(fn(item))  

##推荐
new_list = [fn(item) for item in a_list if condition(item)]

# 列表嵌套
##不推荐
for sub_list in nested_list:
    if list_condition(sub_list):
        for item in sub_list:
            if item_condition(item):
                # do something...  
##推荐
gen = (item for sl in nested_list if list_condition(sl) \
            for item in sl if item_condition(item))
for item in gen:
    # do something...

# 循环嵌套
##不推荐
for x in x_list:
    for y in y_list:
        for z in z_list:
            # do something for x &amp;amp; y  

##推荐
from itertools import product
for x, y, z in product(x_list, y_list, z_list):
    # do something for x, y, z


# 使用any/all函数
##不推荐
found = False
for item in a_list:
    if condition(item):
        found = True
        break
if found:
    # do something if found...  

##推荐
if any(condition(item) for item in a_list):
    # do something if found...

# 属性
##不推荐
class Clock(object):
    def __init__(self):
        self.__hour = 1
    def setHour(self, hour):
        if 25 &amp;gt; hour &amp;gt; 0: self.__hour = hour
        else: raise BadHourException
    def getHour(self):
        return self.__hour

##推荐
class Clock(object):
    def __init__(self):
        self.__hour = 1
    def __setHour(self, hour):
        if 25 &amp;gt; hour &amp;gt; 0: self.__hour = hour
        else: raise BadHourException
    def __getHour(self):
        return self.__hour
    hour = property(__getHour, __setHour)

# with打开文件
with open("some_file.txt") as f:
    data = f.read()
    # 其他文件操作...

# with 忽视异常（python3）
##不推荐
try:
    os.remove("somefile.txt")
except OSError:
    pass

##推荐
from contextlib import ignored  # Python 3 only

with ignored(OSError):
    os.remove("somefile.txt")




