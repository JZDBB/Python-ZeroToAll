f = open('words_weight.txt', 'w+', encoding='utf-8')
list_name = ['SK项目', '小麦项目', '医学图像', 'KG项目', '人脸识别', '虹膜识别', '图片描述', '步态识别']
list_value = [50, 45, 40, 45, 35, 35, 40, 30]
for name, value in zip(list_name, list_value):
    for i in range(value):
        f.write(name)
        f.write('\n')