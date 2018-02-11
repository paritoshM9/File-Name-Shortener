# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 12:31:46 2018

@author: parit
"""



import shutil

import os

#Give the folder location here with double slashes
os.chdir("C:\\Users\\parit\\Documents\\Ethics&Values")

common=""
files=[]

for name in os.listdir('.'):
    files.append(name)

for i in files:
    if(common==""):
        common+=i
    else:
        temp=""
        for j,h in zip(common,i):
            
            if(j==h):
                temp+=j
            else:
                common=temp
                break

address=os.getcwd()

for i in os.listdir('.'):
    n=address+"\\"+i
    shutil.move(n,n.replace(common,"",1))

