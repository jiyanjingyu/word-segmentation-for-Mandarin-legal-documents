#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 22:05:25 2018

@author: joanna
"""
import nltk
import re
import os 
os.chdir("/Users/joanna/Documents")

text = nltk.corpus.udhr.raw(fileids='Chinese_Mandarin-GB2312')
text = text.replace(" ","")
text = re.split("\n+",text)
output = open("result.txt","w")

file = open("list.txt")
word_list = file.read().split("\n")

file2 = open("chengyu.txt")
list1 = file2.read().split("\n")

file3 = open("punctuation.txt")
list2 = file3.read().split("\n")

prelist = list1 + list2

for line in text:
    line2 = line
    segmentation2 = ""
    length_max = max(len(x) for x in word_list)

    length2 = 4
    while line2:

        if line2[-1:] in prelist:
          
            segmentation2 = line2[-1:] + "/" + segmentation2
            line2 = line2[:-1]
        if line2[-4:] in prelist:
          
            segmentation2 = line2[-4:] + "/" + segmentation2
            line2 = line2[:-4]
        elif line2[-3:] in word_list and line2[-3:-2] in prelist:
            
            segmentation2 = line2[-2:] + "/" + segmentation2

            line2 = line2[:-2]
        elif line2[-3:] in word_list:
            segmentation2 = line2[-3:] + "/" + segmentation2
            line2 = line2[:-3]
        elif line2[-2:] in word_list:
            
            segmentation2 = line2[-2:] + "/" + segmentation2
            line2 = line2[:-2]
        else:
            while line2:
                w = line2[-length2:]

                if w in word_list:
                    line2 = line2[:-len(w)]
                    segmentation2 = w + "/" + segmentation2
                    length2 = 4
                    break
                else:
                    if length2 == length_max + 1:
                        w = line2[-1:]
                        line2 = line2[:-len(w)]
                        segmentation2 = w + "/" + segmentation2
                        length2 = 4
                        break
                    else:
                        length2 = length2 + 1
                    
    while re.search("\d/\d",segmentation2):
        segmentation2 = re.sub("(?P<x>\d)/(?P<y>\d)","\g<1>\g<2>",segmentation2)

    while re.search("[A-Z]/[A-Z]",segmentation2):
        segmentation2 = re.sub("(?P<x>[A-Z])/(?P<y>[A-Z])","\g<1>\g<2>",segmentation2)
    while re.search("[一二三四五六七八九十]/[一二三四五六七八九十]",segmentation2):
        segmentation2 = re.sub("(?P<x>[一二三四五六七八九十])/(?P<y>[一二三四五六七八九十])","\g<1>\g<2>",segmentation2)
    segmentation2 = re.sub("有/?必/?要/?","有/必要/",segmentation2)
    segmentation2 = re.sub("每/?个/?人","每个/人",segmentation2)
    segmentation2 = re.sub("每/?一/?个/?人","每/一个/人",segmentation2)
    segmentation2 = re.sub("第(?P<x>[一二三四五六七八九十])","第/\g<1>",segmentation2)
    output.write(segmentation2+"\n")

file.close()
file3.close()
file2.close()
output.close()
