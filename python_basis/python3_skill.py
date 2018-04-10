# -*- coding: utf-8 -*-
"""
python3 技巧篇

"""

"""
1、列表推导式
    bag = [1, 2, 3, 4, 5]
    for i in range(len(bag)):
        bag[i] = bag[i] * 2
    可以写成：
"""
print('1')
bag = [1, 2, 3, 4, 5]
bag = [elem * 2 for elem in bag]
print(bag)

"""
2、遍历列表
    尽量避免这样做：
    bag = [1, 2, 3, 4, 5]
    for i in range(len(bag)):
    print(bag[i])
    取而代之的应该是这样：
    bag = [1, 2, 3, 4, 5]
    for i in bag:
    print(i)
    如果x是一个列表，你可以对它的元素进行迭代。如果你需要各元素索引，那就用enumerate函数。
    如下所示：
"""
print('2')
bag = [1, 2, 3, 4, 5]
for index, element in enumerate(bag):
    print(index, element)


"""
3、元素互换：不需要中间变量
"""
print('3')
a = 1
b = 2
a, b = b, a
print(a, b)

"""
4、初始化列表
"""
print('4')
bag1 = [0] * 10
print(bag1)
bag_of_bags = [[0]] * 5 # [[0], [0], [0], [0], [0]]
bag_of_bags[0][0] = 1 # [[1], [1], [1], [1], [1]]
print(bag_of_bags)
# Oops！所有的列表都改变了，而我们只是想要改变第一个列表
# 改一改啦：
bag_of_bags1 = [[0] for _ in range(5)] # [[0], [0], [0], [0], [0]]
bag_of_bags1[0][0] = 1 # [[1], [0], [0], [0], [0]]
print(bag_of_bags1)

"""
5、构造字符串
    打印字符串。要是有很多变量，避免下面这样：
    name = "Raymond"
    age = 22
    born_in = "Oakland, CA"
    string = "Hello my name is " + name + "and I'm " + str(age) + " years old. I was born in " + born_in + "."
    print(string)
    你可以用.format来代替
    这样做：
"""
print('5')
name = "Raymond"
age = 22
born_in = "Oakland, CA"
string = "Hello my name is {0} and I'm {1} years old. I was born in {2}.".format(name, age, born_in)
print(string)

"""
6、返回
    Python允许你在一个函数中返回多个元素，这让生活更简单。但是在解包元组的时候出出线这样的常见错误：
    def binary:
    return 0, 1
    result = binary
    zero = result[0]
    one = result[1]
    这是没必要的，你完全可以换成这样：
    def binary:
    return 0, 1
    zero, one = binary
    要是你需要所有的元素被返回，用个下划线_：
    zero, _ = binary
"""
print('6')
def binary():
    return 0, 1
zero, one = binary()
print(zero, one)

"""
7、访问
    你也会经常给dicts中写入key，pair（键，值）。
    如果你试图访问一个不存在的于dict的key，可能会为了避免KeyError错误，你会倾向于这样做：
    countr = {}
    bag = [2, 3, 1, 2, 5, 6, 7, 9, 2, 7]
    for i in bag:
        if i in countr:
            countr[i] += 1
        else:
            countr[i] = 1
    for i in range(10):
        if i in countr:
            print("Count of {}: {}".format(i, countr[i]))
        else:
            print("Count of {}: {}".format(i, 0))

"""
print('7')
# 用get是个更好的办法。
countr = {}
bag = [2, 3, 1, 2, 5, 6, 7, 9, 2, 7]
for i in bag:
    countr[i] = countr.get(i, 0) + 1
for i in range(10):
    print("Count of {}: {}".format(i, countr.get(i, 0)))

# 也可以用setdefault来代替。
# 这还用一个更简单却多费点开销的办法：
bag = [2, 3, 1, 2, 5, 6, 7, 9, 2, 7]
countr = dict([(num, bag.count(num)) for num in bag])
for i in range(10):
    print("Count of {}: {}".format(i, countr.get(i, 0)))

# 也可以用dict推导式。
countr = {num: bag.count(num) for num in bag}
# 这两种方法开销大是因为它们在每次count被调用时都会对列表遍历。


"""
8、在列表中切片/步进
    你可以指定start的点和stop点，就像这样list[start:stop:step]。我们取出列表中的前5个元素：
    bag = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for elem in bag[:5]:
        print(elem)
    这就是切片，我们指定stop点是5，再停止前就会从列表中取出5个元素。
    要是最后5个元素怎么做？
    bag = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for elem in bag[-5:]:
        print(elem)
    -5意味着从列表的结尾取出5个元素。
    如果你想对列表中元素间隔操作，你可能会这样做：
    bag = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for index, elem in enumerate(bag):
        if index % 2 == 0:
            print(elem)
"""
print('8')
# 应该这样来做：
bag = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for elem in bag[::2]:
    print(elem)
# 或者用 ranges
bag = list(range(0,10,2))
print(bag)
# 这就是列表中的步进。list[::2]意思是遍历列表同时两步取出一个元素。
# 可以用list[::-1]很酷的翻转列表。

"""
10、tab键还是空格键
    长时间来看，将tab和空格混在一起会造成灾难，你会看到IndentationError: unexpected indent。
    可以在写代码时用空格来定义tab。
    大多数Python用户是用4个空格。
"""







