dict1 = {'Bob':18, 'Alice':17} #形式{键1:值1, 键2:值2}
print(dict1)
print(type(dict1))
#键必须唯一
dict2 = {'乐子':[1, 'a', [2.33, 'Python']], 1:('Hello World!')}
print(dict2)

dict3 = {}
print(type(dict3))
dict4 = dict([('Bob', 18), ('Alice', 17)])
print(dict4)
dict5 = dict((['Bob', 18], ['Alice', 17]))
print(dict5)
dict6 = dict((('Bob', 18), ('Alice', 17)))
print(dict6)
dict7 = dict([['Bob', 18], ['Alice', 17]])
print(dict7)
dict8 = dict(Bob = 18, Alice = 17)
print(dict8)

print(dict1['Bob'])
print('Alice' in dict1)
print('Tom' in dict1)

#更改删除添加字典
dict1['Tom'] = 19
print(dict1)
dict1['Alice'] = 18
print(dict1)
del dict1['Bob']
print(dict1)

print(dict1.keys()) #返回所有key的列表
print(dict1.values()) # 所有value的列表
print(dict1.items()) #返回所有键和值
print(dict2.clear()) #删除元素
print(dict1.get('Alice')) #对应的key对应值
print(dict1.pop('Alice'))
print(dict1)
dict2 = {'a':1, 'b':2}
print(dict2)
print(dict1.update(dict2)) #添加

#遍历
for key in dict1.keys():
	print(key, dict1[key])

#赋值 dict1到dict3 当dict1改变后，dict3也会改变
dict1 = {'Bob':None, 'Tom':19, 'a':1, 'b':2}
dict3 = dict1
print(dict3)
dict1['Bob'] = 19
print(dict1)
print(dict3)
#dict 就像内存中一块区域的指针
print(id(dict1))
print(id(dict3))
#可以发现id是一样的
#因此称作浅复制

#深复制
import copy
print(dict1)

dict4 = copy.deepcopy(dict1)
dict1['Bob'] = None
print(dict1)
print(dict4)
dict1.clear()
print(dict1)
print(dict4)