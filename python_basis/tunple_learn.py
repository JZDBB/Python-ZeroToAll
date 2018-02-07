#tuple
a = 1, 2, 3
print(a)
print(type(a))

tuple1 = ('a', 1, 2.33, [1, 'a'], (1, 3, 5))
print(tuple1)

#创建一个元素元祖时要加逗号
tuple2 = 1,
print(tuple2)
tuple3 = (1)
print(tuple3)
print(type(tuple3)) #result = int
tuple4 = (1,)
print(tuple4)
tuple5 = ()

#基本操作
tuple6 = (1, 2, 3, 4, 5, 6, 7)
print(tuple6[3]) #索引
print(tuple6[-2]) #索引
print(tuple6[1:3]) #切片
print(tuple6[5:3:-1])
tuple7 = (1, 3)
print(tuple6 + tuple7) #连接
print(tuple7 * 3) #复制
for i in tuple6: #对内部元素循环
	print(i)
print(2 in tuple6) #查找元组中是否有某元素
print(0 in tuple6)
del tuple7
print(max(tuple6))
print(min(tuple6))
print(len(tuple6))
print(len(()))

#在元组当中 pop(), append(), extend(), remove(), index() 不可用
#相互转化
print(list(tuple1))
list1 = [1, 2, 3, 4, 5]
print(tuple(list1))

#对比排列组合
print([m+n for m in 'ABC' for n in 'abc']) #list
print([(m,n) for m in 'ABC' for n in 'abc']) #tuple

#元组打包解包
tuple7 = 1, 2, 3, 4
a, b, c, d = tuple7 #一一对应
print(a, b, c, d)