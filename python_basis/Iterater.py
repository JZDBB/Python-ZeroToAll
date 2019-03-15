"""
loop:循环
iterate:迭代
recursion:递归
traversal:遍历
"""

# 迭代器
"""
my_list = ['q', 'w', 'e', 'r', 't', 'y']
my_iter = iter(my_list)
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())

"""


# 文件操作也可以如此。
# with open('1.txt') as f:
#     f.__next__()

# 生成器
class MyRange:
    def __init__(self, n):
        self.i = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


# 生成器函数
def get_odd(lst):
   for i in lst:
       if i % 2:
           yield i

def main():
   lst = range(10)
   for i in get_odd(lst):
       print(i)

if __name__ == '__main__':
    # 生成器测试
    x = MyRange(5)
    print([i for i in x])
    # 生成器函数
    main()
    #生成器表达式
    res = (x for x in range(5))
    print(next(res))
    print(sum((x for x in range(5))))


