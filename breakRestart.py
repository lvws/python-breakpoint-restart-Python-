# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:59:55 2020

@author: Lvws
"""
import time,types,pickle,sys,os
class brestart():

    @classmethod
    def preRunCheck(self):
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
            globals()["aRunlst"] = [x for x in globals()["__dic"]["_nRunlst"]]

    @classmethod
    def add(self):
        globals()['addN'] += 1

    @classmethod
    def filter(self,value):
        filterTp = [types.FunctionType,types.ClassType,types.ModuleType,types.EllipsisType]
        if type(value) == types.ListType:
            for i in value:
                self.filter(i)
        if type(value) == types.DictType:
            for i in value:
                self.filter(value[i])
        if type(value) in filterTp:
            self.add()
        

    @classmethod
    def storeTmp(self):
        keys = globals().keys() # 拿到目前所有的变量（因为是动态的所以）        
        dic = {}
        for key in keys:
            globals()['addN'] = 0
            self.filter(globals()[key])
            if globals()['addN'] != 0 : continue
            dic['_' + key] = globals()[key]
        with open(globals()["__recodefile"],'wb') as f:
            pickle.dump(dic,f)

    @classmethod
    def logFunc(self,func):
        def run(*args,**kargs):
            nRunlst.append(func.__name__) # 记录运行的func
            if globals().get("aRunlst"):          # 如果上次运行过了，就不做了
                globals().get("aRunlst").remove(func.__name__)
                print "Pass"
                return 
            # Once going to Run new task transfer info to globals 
            if globals()["__runtag"] == 0:       
                for key in globals()["__dic"]:
                    if key == "___dic":continue
                    globals()[key[1:]] = globals()["__dic"][key]
                globals()["__runtag"] = 1

            now = time.time()
            print "Now Running: " + func.__name__
            func(*args,**kargs)
            print "function over,use time: " + str((time.time() - now))
            self.storeTmp() # recode every success run
        return run

    @classmethod
    def end(self):
        os.remove(globals()["__recodefile"])