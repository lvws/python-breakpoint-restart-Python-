# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:59:55 2020

@author: Administrator
"""
import time,types



def logFunc(func):
    def run(*args,**kargs):
        nRunlst.append(func.__name__) # 记录运行的func
        if p.get("aRunlst"):          # 如果上次运行过了，就不做了
            p.get("aRunlst").remove(func.__name__)
            print "Pass"
            return 
        now = time.time()
        print "Now Running: " + func.__name__
#        print "args:",args,kargs
        func(*args,**kargs)
        print "function over,use time: " + str((time.time() - now))
        print p['age']    
    
    return run

@logFunc
def printf(*args):
    for key in args:
        time.sleep(0.2)
        print key
        
@logFunc    
def add(age):
    time.sleep(1)
    age+=1
    print "age:" , age
    
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age


p = locals() # 动态记录所有的变量
nRunlst = [] # 记录已经运行的func
aRunlst = ['printf','add','printf'] # 模拟上一次运行过的func 列表

name = "XiangoMin"
age = 12 
peple = {"name":name,"age":age}
lst = [1,2,4,'xx']
xim = Person(name,age) 

# 运行的func    
printf("helo",'ok','java')
add(10)
printf("good",[1,2,3,4],"jj",'dog')
add(20)

print nRunlst 

keys = p.keys() # 拿到目前所有的变量（因为是动态的所以）

filterTp = [types.FunctionType,types.ClassType,types.ModuleType]
for key in keys:
    if type(p[key]) in filterTp:
        continue
    print key,p[key]
