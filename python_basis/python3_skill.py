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
print('1、')
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
print('2、')
bag = [1, 2, 3, 4, 5]
for index, element in enumerate(bag):
    print(index, element)


"""
3、元素互换：不需要中间变量
"""
print('3、')
a = 1
b = 2
a, b = b, a
print(a, b)

"""
4、初始化列表
"""
print('4、')
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
print('5、')
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
print('6、')
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
print('7、')
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
print('8、')
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
9、遍历两个集合
    更好的方法
    zip在内存中生成一个新的列表，需要更多的内存。izip比zip效率更高。
    注意：在Python 3中，izip改名为zip，并替换了原来的zip成为内置函数。
"""
print('9、')
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']
for name, color in zip(names, colors):
    print(name, '--->', color)


"""
10、tab键还是空格键
    长时间来看，将tab和空格混在一起会造成灾难，你会看到IndentationError: unexpected indent。
    可以在写代码时用空格来定义tab。
    大多数Python用户是用4个空格。
"""


"""
11、自定义排序顺序
    colors = ['red', 'green', 'blue', 'yellow']
    def compare_length(c1, c2):
        if len(c1) < len(c2): return -1
        if len(c1) > len(c2): return 1
        return 0
    print sorted(colors, cmp=compare_length)
    更好的方法:
    print sorted(colors, key=len)
    第一种方法效率低而且写起来很不爽。另外，Python 3已经不支持比较函数了。

"""
print('11、')
colors = ['red', 'green', 'blue', 'yellow']
print(sorted(colors, key=len))

"""
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i
    for执行完所有的循环后就会执行else。
"""


"""
12、遍历字典的key
    d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
    for k in d:
        print k
    for k in d.keys():
        if k.startswith('r'):
            del d[k]
    什么时候应该使用第二种而不是第一种方法？当你需要修改字典的时候。
    如果你在迭代一个东西的时候修改它，那就是在冒天下之大不韪，接下来发生什么都活该。
    d.keys()把字典里所有的key都复制到一个列表里。然后你就可以修改字典了。
    注意：如果在Python 3里迭代一个字典你得显示地写：list(d.keys())，因为d.keys()返回的是一个“字典视图”(一个提供字典key的动态视图的迭代器)。详情请看文档
"""

"""
13、提高可读性
    "位置参数和下标很漂亮
     但关键字和名称更好
     第一种方法对计算机来说很便利
     第二种方法和人类思考方式一致"

    (1)用关键字参数提高函数调用的可读性
    twitter_search('@obama', False, 20, True)
    更好的方法
    twitter_search('@obama', retweets=False, numtweets=20, popular=True)

    (2)第二种方法稍微(微秒级)慢一点，但为了代码的可读性和开发时间，值得。
    用namedtuple提高多个返回值的可读性
    # 老的testmod返回值
    doctest.testmod()
    # (0, 4)
    # 测试结果是好是坏？你看不出来，因为返回值不清晰。
    更好的方法
    # 新的testmod返回值, 一个namedtuple
    doctest.testmod()
    # TestResults(failed=0, attempted=4)
    namedtuple是tuple的子类，所以仍适用正常的元组操作，但它更友好。
    创建一个nametuple
    TestResults = namedTuple('TestResults', ['failed', 'attempted'])
    unpack序列
    p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'

    # 其它语言的常用方法/习惯
    fname = p[0]
    lname = p[1]
    age = p[2]
    email = p[3]
    更好的方法
    fname, lname, age, email = p

    第二种方法用了unpack元组，更快，可读性更好。
    更新多个变量的状态
    def fibonacci(n):
        x = 0
        y = 1
        for i in range(n):
            print x
            t = y
            y = x + y
            x = t
    更好的方法
    def fibonacci(n):
        x, y = 0, 1
        for i in range(n):
            print x
            x, y = y, x + y
    第一种方法的问题
    x和y是状态，状态应该在一次操作中更新，分几行的话状态会互相对不上，这经常是bug的源头。
    操作有顺序要求
    太底层太细节
    第二种方法抽象层级更高，没有操作顺序出错的风险而且更效率更高。
"""

"""
    14、lambda表达式——【lambda 参数:操作(参数)】
"""
add = lambda x, y: x + y
print(add(1, 2))
#列表排序
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)
# 列表并行排序
data = zip([1, 3, 2, 4, 8, 5], [7, 3, 8, 2, 0])
data = sorted(data)
list1, list2 = map(lambda t: list(t), zip(*data))
print(list1, list2)

