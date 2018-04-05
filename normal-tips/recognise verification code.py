# -*- coding: utf-8 -*-
# python2语法 仍需要调试 pytesser包异常导入
# 1、导入Image包，打开图片：

from PIL import Image
from pytesser import pytesser
image = Image.open('7039.jpg')
print pytesser.image_file_to_string('7039.jpg')
print pytesser.image_to_string(image)

# 2、把彩色图像转化为灰度图像。RBG转化到HSI彩色空间，采用I分量：

imgry = image.convert('L')
imgry.show()


# 3、二值化处理
# 二值化是图像分割的一种常用方法。在二值化图象的时候把大于某个临界灰度值的像素灰度设为灰度极大值，
# 把小于这个值的像素灰度设为灰度极小值，从而实现二值化（一般设置为0-1）。根据阈值选取的不同，
# 二值化的算法分为固定阈值和自适应阈值，这里选用比较简单的固定阈值。
# 把像素点大于阈值的设置,1，小于阈值的设置为0。生成一张查找表，再调用point()进行映射。

threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')
out.show()

# 更多：https://blog.csdn.net/hk_jh/article/details/8961449

