#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import MeCab
import random
import re

def marcov_generate(file_name):
    f=open(file_name,'r',encoding='utf-8')
    text=f.read()
    f.close

    mt=MeCab.Tagger('-Owakati')
    mt.parse('')
    
    word_list=mt.parse(text)
    word_list=word_list.rstrip('\n').split(' ')

    markov={}
    w=''
    for x in word_list:
        if w:
            if w in markov:
                new_list=markov[w]
            else:
                new_list=[]

            new_list.append(x)
            markov[w]=new_list
        w=x
    
    choice_words=word_list[0] #毎回起動時のひとこと目を固定してる。
    sentence=""
    count=0

    while count < 90:
        sentence += choice_words
        choice_words=random.choice(markov[choice_words])
        count += 1

        sentence=sentence.split(' ',1)[0]
        p=re.compile('[-/:-@[-`{-~]') #!は外してもいいかもしれない
        sus=p.sub('',sentence)

    words=re.sub(re.compile('[-~]'),'',sus) #同上
    print(words)
    
if __name__=='__main__':
    file_name=sys.argv[1]
    marcov_generate(file_name)
