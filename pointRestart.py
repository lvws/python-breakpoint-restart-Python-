# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:59:55 2020

@author: Administrator
"""
import time,types,pickle,sys,os

def storeTmp():
    keys = globals().keys() # 拿到目前所有的变量（因为是动态的所以）
    filterTp = [types.FunctionType,types.ClassType,types.ModuleType]
    dic = {}
    for key in keys:
        if type(globals()[key]) in filterTp:
            continue
        dic['_' + key] = globals()[key]
    print dic
    with open(globals()["__recodefile"],'wb') as f:
        pickle.dump(dic,f)

def logFunc(func):
    def run(*args,**kargs):
        nRunlst.append(func.__name__) # 记录运行的func
        if globals().get("aRunlst"):          # 如果上次运行过了，就不做了
            globals().get("aRunlst").remove(func.__name__)
            print "Pass"
            return 
        # Once going to Run new task transfer info to globals 
        if globals()["__runtag"] == 0:            
            for key in __dic:
                if key == "___dic":continue
                globals()[key[1:]] = __dic[key]
            globals()["__runtag"] = 1

        now = time.time()
        print "Now Running: " + func.__name__
        func(*args,**kargs)
        print "function over,use time: " + str((time.time() - now))
        storeTmp() # recode every success run
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
        

def preRunCheck():
    __recodefile = os.path.join(os.path.dirname(sys.argv[0]),'.'+os.path.basename(sys.argv[0])+'.pkl')
    globals()["__recodefile"] = __recodefile
    globals()["__runtag"] = 0
    globals()["aRunlst"] = []
    globals()["nRunlst"] = []
    globals()["__dic"] = {}
    if os.path.exists(__recodefile):
        f = open(__recodefile,'rb')
        globals()["__dic"] = pickle.load(f)
        f.close()
        globals()["aRunlst"] = [x for x in __dic["_nRunlst"]]

    
        




 # 动态记录所有的变量
#nRunlst = [] # 记录已经运行的func
#aRunlst = ['printf','add','printf'] # 模拟上一次运行过的func 列表

preRunCheck()
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

print nRunlst 
<<<<<<< HEAD



=======
>>>>>>> eb4f326cfd390c22d98a1de5a62e01932f6aeae9
