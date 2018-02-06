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
        