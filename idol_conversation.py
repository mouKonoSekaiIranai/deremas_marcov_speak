#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import MeCab
import random
import re
import requests
import time
from bs4 import BeautifulSoup

class Idol_speak(object):
    def __init__(self,idol_name):
        self.idol_name=self.check_is_argv(idol_name)
        self.get_idol_speak()
        
    def check_is_argv(self,idol_name):
        if idol_name==None:
            print('Please tell me your favorite idol. ->')
            idol_name=input()        
        return idol_name

    def get_idol_speak(self):
        idol_name=self.idol_name
        idol_bf=self.request_idol()
        self.get_speak_str(idol_bf)
        
    def request_idol(self):
        idol_name=self.idol_name
        wiki_url='https://imascg-slstage-wiki.gamerch.com/'
        idol_url=wiki_url+idol_name
        responce=requests.get(idol_url)
        idol_bf=BeautifulSoup(responce.text,'lxml')
        idol_bf.prettify()
        return idol_bf

    def get_speak_str(self,idol_bf):
        idol_name=self.idol_name
        idol_speak=""
        for speak in idol_bf.select('tr > td[style*="text-align:left;"]'):
            if speak.text=="":
                continue
            idol_speak+=speak.text
            idol_speak.split()
            idol_speak+='\n'
        file_name=idol_name+".txt"
        f=open(file_name,"w")
        f.write(idol_speak)
        print('Success get to ',idol_name,'\'s speaks.')
        print('file name is ',file_name,'.')
        f.close

    def marcov_generate(self,talk_topic):        
        f=open(self.idol_name+'.txt','r',encoding='utf-8')
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
        choice_words=''
        if talk_topic in word_list:
            choice_words=talk_topic
        else:
            choice_words=random.choice(word_list)
        sentence=""
        sus=""
        count=0        
        while count<25 and (sus[-1:]!='。' or sus[-1:]!='!' or sus[-1:]!='?'):
            sentence += choice_words
            choice_words=random.choice(markov[choice_words])
            count += 1
            sentence=sentence.split(' ',1)[0]
            p=re.compile('[-/:-@[-`{-~]')
            sus=p.sub('',sentence)
        words=re.sub(re.compile('[-~]'),'',sus)        
        return words

    def conversation(self):       
        user_name='あなた'
        idol_name=self.idol_name
        print(user_name,' : ')
        user_speak=input()
        mt=MeCab.Tagger('')
        mt.parse('')
        topic_list=[]
        node=mt.parseToNode(user_speak)
        talk_topic=''
        while node:
            surface=node.surface
            meta=node.feature.split(',')
            if meta[0]==('名詞'):
                topic_list.append(node)
            node=node.next
        if topic_list==[]:
            talk_topic=None
        else:
            talk_topic=random.choice(topic_list)

        print('talk_topic :',talk_topic.surface)
        idol_responce=self.marcov_generate(talk_topic)
        print(idol_name,' : ',idol_responce)


if __name__=='__main__':
    idol_name=''
    if len(sys.argv)==2:
        idol_name=sys.argv[1]
    else:
        idol_name=None
    idol_speak=Idol_speak(idol_name)
    while True:
        idol_speak.conversation()
        time.sleep(1)
