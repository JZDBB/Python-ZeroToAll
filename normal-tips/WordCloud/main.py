"""
wordcloud.WordCloud(
    font_path=None,  # 字体路径，英文不用设置路径，中文需要，否则无法正确显示图形
    width=400, # 默认宽度
    height=200, # 默认高度
    margin=2, # 边缘
    ranks_only=None,
    prefer_horizontal=0.9,
    mask=None, # 背景图形，如果想根据图片绘制，则需要设置
    scale=1,
    color_func=None,
    max_words=200, # 最多显示的词汇量
    min_font_size=4, # 最小字号
    stopwords=None, # 停止词设置，修正词云图时需要设置
    random_state=None,
    background_color='black', # 背景颜色设置，可以为具体颜色,比如white或者16进制数值
    max_font_size=None, # 最大字号
    font_step=1,
    mode='RGB',
    relative_scaling='auto',
    regexp=None,
    collocations=True,
    colormap='viridis', # matplotlib 色图，可更改名称进而更改整体风格
    normalize_plurals=True,
    contour_width=0,
    contour_color='black',
    repeat=False)
"""
import os
from os import path
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from scipy.misc import imread
import random

def wc_english():
    # 获取当前文件路径
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    # 获取文本text
    text = open(path.join(d,'1.txt')).read()
    # 读取背景图片
    background_Image = np.array(Image.open(path.join(d, "1.jpg")))
    # or
    # background_Image = imread(path.join(d, "mask1900.jpg"))
    # 提取背景图片颜色
    img_colors = ImageColorGenerator(background_Image)
    # 设置英文停止词
    stopwords = set(STOPWORDS)
    wc = WordCloud(
        margin = 2, # 设置页面边缘
        mask = background_Image,
        scale = 2,
        max_words = 200, # 最多词个数
        min_font_size = 4, # 最小字体大小
        stopwords = stopwords,
        random_state = 42,
        background_color = 'white', # 背景颜色
        max_font_size = 150, # 最大字体大小
        )
    # 获取文本词排序，可调整 stopwords
    process_word = WordCloud.process_text(wc, text)
    sort = sorted(process_word.items(), key=lambda e: e[1], reverse=True)
    # print(sort[:50])  # 获取文本词频最高的前50个词
      # 结果
    # [('one', 60), ('ship', 47), ('Nineteen Hundred', 43), ('know', 38), ('music', 36), ...]
    stopwords = set(STOPWORDS)
    stopwords.add('know')
    stopwords.add('end')
    # 生成词云
    wc.generate_from_text(text)
    # 等价于
    # wc.generate(text)
    # 根据图片色设置背景色
    wc.recolor(color_func=img_colors)
    #存储图像
    wc.to_file('1900pro1.png')
    # 显示图像
    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    wc_english()