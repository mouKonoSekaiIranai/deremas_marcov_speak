#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import MeCab
import sys

file_name=sys.argv[1]
fp=open(file_name,'r')
text=fp.read()
fp.close()

mt=MeCab.Tagger()
mt.parse('')

word_dict={}
lines=text.split('\n')
for line in lines:
    word_list=mt.parse(line)
    word_list=word_list.rstrip('\n').split(' ')
    print(word_list)
