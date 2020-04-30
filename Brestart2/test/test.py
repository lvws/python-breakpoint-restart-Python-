# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 13:43:17 2020

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:59:55 2020

@author: Lvws
"""

from Brestart2 import Brestart
import os,sys,time

@Brestart.logFuncTest
def printf(*args):
    for key in args:
        time.sleep(0.2)
        print(key)

@Brestart.logFuncTest
def add(age):
    time.sleep(1)
    age+=1
    print("age:" , age)

def genN(x):
    while True:        
        x +=1
        yield x

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    Brestart.preRunCheck()
    name = "XiangoMin"
    age = 12 
    peple = {"name":name,"age":age}
    lst = [1,2,4,'xx']
    xim = Person(name,age)
    gen = genN(0)

    next(gen) # 1
    next(gen) # 2

    # 运行的func
    printf("helo",'ok','java')
    add(10)
    print(next(gen)) #3
    #sys.exit(1)
    printf("good",[1,2,3,4],"jj",'dog')
    add(20)

    Brestart.end()