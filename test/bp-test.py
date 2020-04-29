# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:59:55 2020

@author: Lvws
"""

from breakRestart import *
import os,sys

@Brestart.logFuncTest
def printf(*args):
    for key in args:
        time.sleep(0.2)
        print key

@Brestart.logFuncTest
def add(age):
    time.sleep(1)
    age+=1
    print "age:" , age
    
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

if __name__ == "__main__":
    Brestart.preRunCheck()
    name = "XiangoMin"
    name = "XiangoMin"
    age = 12 
    peple = {"name":name,"age":age}
    lst = [1,2,4,'xx']
    xim = Person(name,age) 

    # 运行的func
    printf("helo",'ok','java')
    add(10)
    #sys.exit(1)
    printf("good",[1,2,3,4],"jj",'dog')
    add(20)

    Brestart.end()