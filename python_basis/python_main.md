# Python main knowledge

###  Python中 *args 和 **kwargs 的区别

```
def foo(*args, **kwargs):
    print 'args = ', args
    print 'kwargs = ', kwargs
    print '---------------------------------------'

if __name__ == '__main__':
    foo(1,2,3,4)
    foo(a=1,b=2,c=3)
    foo(1,2,3,4, a=1,b=2,c=3)
    foo('a', 1, None, a=1, b='2', c=3)

```
最后的输出

```
args =  (1, 2, 3, 4) 
kwargs =  {} 
--------------------------------------- 
args =  () 
kwargs =  {'a': 1, 'c': 3, 'b': 2} 
--------------------------------------- 
args =  (1, 2, 3, 4) 
kwargs =  {'a': 1, 'c': 3, 'b': 2} 
--------------------------------------- 
args =  ('a', 1, None) 
kwargs =  {'a': 1, 'c': 3, 'b': '2'} 
---------------------------------------
```

可以看到，这两个是python中的可变参数。`*args`表示任何多个无名参数，它是一个tuple；`**kwargs`表示关键字参数，它是一个dict。并且同时使用`*args`和`**kwargs`时，必须`*args`参数列要在`**kwargs`前，像`foo(a=1, b='2', c=3, a', 1, None, )`这样调用的话，会提示语法错误`“SyntaxError: non-keyword arg after keyword arg”`。



### closure 

closure(闭包)：**闭包=函数+自由变量的引用**

```Python
def outer():
    var = 3
    def inner():
        print var
    return inner

func = outer()
func()   # print 3
var = 5
func()   # print 3
```

这段代码中，函数inner和var就构成了闭包，var对于inner来说就是自由变量。可以看到var不是在inner中定义的，而是在outer中定义。当func=outer()执行结束，按道理var的引用计数为0，应该被GC回收了，可是执行func()却没报错，打印出了var的值！这说明var的引用仍然存在，这个引用在哪呢？答案就是函数inner.__code__.co_freevars和inner.__closure__，前者记录了自由变量的名字，后者记录了自由变量的值。	

```python
print func.__code__.co_freevars # ('var',)
print func.__closure__[0].cell_contents # 3
```

