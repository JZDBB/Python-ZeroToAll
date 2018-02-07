set1 = {1, 2, 3, 4, 5}
print(set1)
set2 = {1, 2.33, 'Python', (1, 'b')}
print(set2)
print(type(set1))
set4 = set()
print(set4)

#set(tuple/list) 为元组和列表的转换
set5 = set('Python')
set6 = {1, 2, 3, 4, 5}
print(set6)
set6.add('a')
print(set6)

set7 = {'b', 'c'}
set6.update(set7)
print(set6)

print(set6.pop())
print(set6)
print(set6.pop())
print(set6)

set6.remove(3)
print(set6)
# set6.remove(1) -> error

#删除集合中的元素，如果元素不存在则不做
set6.discard(1)
print(set6)
set6.discard(5)
print(set6)

set7.clear()
print(set7)

#集合操作
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}
print(set_1.intersection(set_2)) #交集
print(set_1.union(set_2)) #并集
print(set_1.difference(set_2)) #差集

print(1 in set_1)
print(6 in set_1)

set_3 = {1, 2, 3}
print(set_3.issubset(set_1))
set_4 = {1, 1.1}
print(set_4.issubset(set_1))
