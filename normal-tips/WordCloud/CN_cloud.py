# # -*- coding: utf-8 -*-
# import jieba
# import os
# import codecs
# from scipy.misc import imread
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#
#
# class GetWords(object):
#     def __init__(self, dict_name, file_list, dic_list):
#         self.dict_name = dict_name
#         self.file_list = file_list
#         self.dic_list = dic_list
#
#     # 获取自定义词典
#     def get_dic(self):
#         dic = open(self.dict_name, 'r')
#         while 1:
#             line = dic.readline().strip()
#             self.dic_list.append(line)
#             if not line:
#                 break
#             pass
#
#     def get_word_to_cloud(self):
#         for file in self.file_list:
#             with codecs.open('../spider/' + file, "r", encoding='utf-8', errors='ignore') as string:
#                 string = string.read().upper()
#                 res = jieba.cut(string, HMM=False)
#                 reslist = list(res)
#                 wordDict = {}
#                 for i in reslist:
#                     if i not in self.dic_list:
#                         continue
#                     if i in wordDict:
#                         wordDict[i] = wordDict[i] + 1
#                     else:
#                         wordDict[i] = 1
#
#             coloring = imread('test.jpeg')
#
#             wc = WordCloud(font_path='msyh.ttf', mask=coloring,
#                            background_color="white", max_words=50,
#                            max_font_size=40, random_state=42)
#
#             wc.generate_from_frequencies(wordDict)
#
#             wc.to_file("%s.png" % (file))
#
#
# def set_dic():
#     _curpath = os.path.normpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
#     settings_path = os.environ.get('dict.txt')
#     if settings_path and os.path.exists(settings_path):
#         jieba.set_dictionary(settings_path)
#     elif os.path.exists(os.path.join(_curpath, 'data/dict.txt.big')):
#         jieba.set_dictionary('data/dict.txt.big')
#     else:
#         print("Using traditional dictionary!")
#
#
# if __name__ == '__main__':
#     set_dic()
#     file_list = ['data_visualize.txt', 'data_dev.txt', 'data_mining.txt', 'data_arc.txt', 'data_analysis.txt']
#     dic_name = 'dict.txt'
#     dic_list = []
#     getwords = GetWords(dic_name, file_list, dic_list)
#     getwords.get_dic()
#     getwords.get_word_to_cloud()


# -*-coding:utf-8-*-

###生成txt文件的词云

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import jieba
from PIL import Image
import numpy as np
import os
from os import path

text = open("fenciHou1.txt", "rb").read().decode('utf-8')
# text = open("cv.txt", "rb").read()
# 结巴分词
# wordlist = jieba.cut(text, cut_all=True)
# wl = " ".join(wordlist)
# print(wl)#输出分词之后的txt
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
background_Image = np.array(Image.open(path.join(d, "1545566997_781739.png")))
# or
# background_Image = imread(path.join(d, "mask1900.jpg"))
# 提取背景图片颜色
img_colors = ImageColorGenerator(background_Image)
# 把分词后的txt写入文本文件
# fenciTxt  = open("fenciHou.txt","w+", encoding='utf-8')
# fenciTxt.writelines(wl)
# fenciTxt.close()


# 设置词云
wc = WordCloud(background_color="black",  # 设置背景颜色
               margin = 2, # 设置页面边缘
               mask=background_Image,# mask = "图片",  #设置背景图片
               max_words=500,  # 设置最大显示的字数
               # stopwords = "", #设置停用词
               font_path="fangsong_GB2312.ttf",
               # 设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文）
               max_font_size=200,  # 设置字体最大值
               min_font_size=5, # 最小字号
               collocations=False, # 不重复显示词语
               colormap='viridis', # matplotlib 色图，可更改名称进而更改整体风格
               random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
               mode='RGB'
               )
myword = wc.generate(text)  # 生成词云
wc.recolor(color_func=img_colors)
    #存储图像
wc.to_file('12.png')
# 展示词云图
plt.imshow(myword)
plt.axis("off")
plt.show()
