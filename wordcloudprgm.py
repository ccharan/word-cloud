# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 22:18:17 2020

@author: hp
"""

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

text = "Happy Birthday Charan"

wordcloud = WordCloud(repeat=10, max_words=30, width=1280, height=720).generate(text)

wordcloud.to_file("C:\Users\hp\img.png")



plt.axis("off")
plt.imshow(wordcloud, interpolation='bilinear')
plt.show()



