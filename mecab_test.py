#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import MeCab
import random
import re

def mecab_file():
    f=open(file,'r',encoding='utf-8').read()
    text=f.read()
    f.close
    

if __name__=='__main__':
    file=sys.argv[1]
    raw=open(file,'r',encoding='utf-8').read()
    print(raw)
    m=MeCab.Tagger('-Ochasen')
    m.parse('')
    node=m.parseToNode(raw)
    while node:
        try:
            print(node.surface)
        except:
            pass
        node=node.next
