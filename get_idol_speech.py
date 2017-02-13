#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys

class Idol_speech(object):
    def __init__(self,idol_name):
        self.idol_name=self.check_is_argv(idol_name)
        self.get_idol_speech()
        
    def check_is_argv(self,idol_name):
        if idol_name==None:
            print('Please tell me your favorite idol. ->')
            idol_name=raw_input()        
        return idol_name

    def get_idol_speech(self):
        idol_name=self.idol_name
        idol_bf=self.request_idol()
        self.get_speech_str(idol_bf)
        
    def request_idol(self):
        idol_name=self.idol_name
        wiki_url='https://imascg-slstage-wiki.gamerch.com/'
        idol_url=wiki_url+idol_name
        responce=requests.get(idol_url)
        idol_bf=BeautifulSoup(responce.text,'lxml')
        idol_bf.prettify()
        return idol_bf

    def get_speech_str(self,idol_bf):
        idol_name=self.idol_name
        idol_speech=""
        for speech in idol_bf.select('tr > td[style*="text-align:left;"]'):
            if speech.text=="":
                continue
            print(speech.text)
            idol_speech+=speech.text
            idol_speech.split()
            idol_speech+='\n'
        file_name=idol_name+".txt"
        f=open(file_name,"w")
        f.write(idol_speech)
        print('Success get to ',idol_name,'\'s speechs.')
        print('file name is ',file_name,'.')
        f.close

    def 
        
if __name__=='__main__':
    idol_speech=Idol_speech('赤城みりあ')
