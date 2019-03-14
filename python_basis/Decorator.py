# 「装饰器」本质上就是一个函数，这个函数的特点是可以接受其它的函数当作它的参数，
# 并将其替换成一个新的函数（即返回给另一个函数）——也就是嵌套
# 优点：使用了装饰器可读性更好了一些

def first(fun):
    def second():
        print('start')
        fun()
        print('end')
        print(fun.__name__)
    return second

# def man():
#     print('i am a man()')
#
# f = first(man)
# f()

# # 「@frist」在 man 函数的上面，表示对 man 函数使用 first 装饰器。「@」 是装饰器的语法，「first」是装饰器的名称。
# @first # 语法糖 省略了first(man)
# def man():
#     print('i am a man()')
#
# man()

# 特殊在多了检查当前用户是否为 admin 这步判断，如果当前用户不是 admin，则抛出异常。
def check_admin(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception('This user do not have permission')
        return func(*args, **kwargs)
    return wrapper

class Stack:
    def __init__(self):
        self.item = []

    @check_admin
    def push(self, username, item):
        self.item.append(item)

    @check_admin
    def pop(self, username):
        if not self.item:
            raise Exception('NO elem in stack')
        return self.item.pop()

sta = Stack()
sta.item.append('admin')
sta.push('admin', username='admin')
sta.push('YN')
sta.pop('admin')
sta.pop('QY')

# # 带参数的装饰器
# import logging
# def use_logging(level):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if level == "warn":
#                 logging.warn("%s is running" % func.__name__)
#             elif level == "info":
#                 logging.info("%s is running" % func.__name__)
#             return func(*args)
#         return wrapper
#
#     return decorator
#
# @use_logging(level="warn")
# def foo(name='foo'):
#     print("i am %s" % name)
#
# foo()

# # 类装饰器
# class Foo(object):
#     def __init__(self, func):
#         self._func = func
#
#     def __call__(self):
#         print ('class decorator runing')
#         self._func()
#         print ('class decorator ending')
#
# @Foo
# def bar():
#     print('bar')
#
# bar()
#
# # wrap
# from functools import wraps
# def logged(func):
#     @wraps(func)
#     def with_logging(*args, **kwargs):
#         print(func.__name__)     # 输出 'f'
#         print(func.__doc__)     # 输出 'does some math'
#         return func(*args, **kwargs)
#     return with_logging
#
# @logged
# def f(x):
#    """does some math"""
#    return x + x * x

