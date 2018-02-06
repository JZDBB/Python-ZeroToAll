    list_1 = [1, 2, 3, 4]
    print(list_1)

    list_2 = ['a', 'b', 'c']
    print(list_2)

    list_3 = [1, 2.33, 'python', 'a']
    print(list_3)

    list_4 = [1, 3.3, 'haha', list_3]
    print(list_4)

    list_5 = []
    type(list_5)

    #索引
    print(list_1[0])
    print(list_3[2])

    #连接
    print(list_1 + list_2)

    #复制阵列
    print(list_1 * 3)

    #列表长度
    len(list_2)

    for i in list_1:
    	print(i)

    #是否存在
    2 in list_1
    6 in list_1

    #删除
    del list_1
    del list_2[2]

    #返回最大/小值
    max(list_2)
    min(list_2)

    #索引 [起始:终止:间隔]
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    list_1[5:8]
    list_1[1:6:2]
    list_1[3:]
    list_1[:5]
    list_1[::2]
    list_1[::-1]#逆序索引

    #id操作？？
    id(list_1)
    id(list_1[:])
    list_6 = list_1[:]
    id(list_6) 

    #改变数据
    list_1[2] = 'python'
    list_1[4:6] = ['a', 'b', 'c']
    print(list_1)

    #增加对象
    list_1.append('Alice')
    list_1.append(1)
    list_1.append('1')

    #次数统计
    list_1.count(1)
    list_1.count('1')

    #追加
    list_2
    list_2.extend('a')
    list_2
    list_2.extend(['b', [1, 2, 3]])

    #索引位置找到第一个所在
    list_3 = [1, 2, 3, 3, 5, 2, 7, 8]
    list_3.index(1)
    list_3.index(2)

    list_3
    list_3.insert(2, 'a')
    list_3

    list_3.pop()
    list_3
    list_3.pop(2)
    list_3

    #移走某一个匹配值
    list_3.remove(2)

    #反向
    list_3
    list_3.reverse()
    list_3
    list_3[::-1]

    #排序
    list_3 = [2, 4, 1, 3, 6, 8, 5, 9, 0]
    list_3.sort()
    list_3
    list_7 = ['a', 'cc', '1', 'Python']
    list_7.sort()
    list_7
    list_7.sort(reverse = True)

    [i**2 for i in range(1,10)]
    [i*j for j in range(1,i) for i in range(1,10) if j<=i]
    [m+n for m in 'ABC' for n in 'abc']
    