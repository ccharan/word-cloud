# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 17:30:03 2021

@author: Charan C
"""

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# file path to save
path = "C:\\Users\\hp\\Downloads\\temp\\" 

# words to be used to create the word cloud greetings
text = "Happy New Year friendshp Happy New Year fit joy prosper win "

# person names to be displayed in the greeting card (Customize)
names = ['charan ', 'Hari ']

for name in names:
    # contenating the text with name(repeat the name 3 times)
    wishes = text + name * 3

    wordcloud = WordCloud(repeat=10, max_words=30, width=1280, height=720).generate(wishes)
    
    # save the file to the path
    wordcloud.to_file(path + name + ".png")

    # displaying the image on the terminal itself for preview
    plt.axis("off")
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.show()

