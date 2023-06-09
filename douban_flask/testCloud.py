# -*- coding: utf-8 -*-
# @Time    : 2022/9/11 16:27
# @Author  : Lason
# @FileName: testCloud.py
# @Software: PyCharm

import jieba            # 分词
import matplotlib.pyplot as plt     # 绘图  可视化
from wordcloud import WordCloud     # 词云
from PIL import Image       # 图像处理
import numpy as np          # 矩阵运算
import sqlite3      # 数据库

# 1.准备词云所需要的文字（词）
conn = sqlite3.connect("movie_top250.db")
cursor = conn.cursor()
sql = "select introduction from movie250"
text = ""
data = cursor.execute(sql)
for item in data:
    text = text + item[0]
# print(text)
cursor.close()
conn.close()

# 2. 分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))
print(string)

img = Image.open(r'.\static\assets\img\tree.jpg')     # 打开遮罩图片
img_array = np.array(img)       # 生成数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="msyh.ttc"            # 字体所在位置    C:\Windows\Fonts
)
wc.generate_from_text(string)       # 生成遮罩图

# 绘制图片

flag = plt.figure(1)
plt.imshow(wc)
plt.axis('off')     # 是否显示坐标轴

# plt.show()      # 显示生成的云图片

# 输出词云图片到文件
plt.savefig(r'.\static\assets\img\word.png', dpi=500)


















