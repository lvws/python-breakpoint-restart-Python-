# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 15:59:55 2020

@author: Lvws
email: 1129309258@qq.com
github: https://github.com/lvws/python-breakpoint-restart-Python-

Function:
this module make it easy for any python script recorde results after some time-consuming task;
so if some unpredictable errors happened and crashed your script, it can pass the funcs that has already 
successfully finished, just begin from the breakpoint;

Method:
a. before run your task,import this module, and at the fist run step --  Brestart.preRunCheck() ;
check if something wrong ,and wether it needs breakpoint restart;
b. use @Brestart.logFunc to decorate the functions that cost much time,make it a recorde point;
c. finally Brestart.end() at the last run step ,can clear temp log and do not affect next run. 
"""

import time,types,pickle,sys,os

class Brestart():

    @classmethod
    def preRunCheck(self):
        """
        check if something wrong at last time running,and get the info from the log file.
        """
        __recodefile = os.path.join(os.path.dirname(sys.argv[0]),'.'+os.path.basename(sys.argv[0])+'.pkl')
        globals()["__recodefile"] = __recodefile
        globals()["__runtag"] = 0
        globals()["_aRunlst"] = []
        globals()["_nRunlst"] = []
        globals()["__dic"] = {} 
        if os.path.exists(__recodefile):
            f = open(__recodefile,'rb')
            globals()["__dic"] = pickle.load(f)
            f.close()
            globals()["_aRunlst"] = [x for x in globals()["__dic"]["__nRunlst"]]

    # recode if the variable can be pickled, 
    @classmethod
    def add(self):
        globals()['_addN'] += 1

    @classmethod
    def filter(self,value):
        filterTp = [types.FunctionType,types.new_class,types.prepare_class,types.ModuleType] # types cannot be picked
        if type(value) == list:
            for i in value:
                self.filter(i)
        if type(value) == dict:
            for i in value:
                self.filter(value[i])
        if type(value) in filterTp:
            self.add()
        
    # recode runinfo and write to log file
    @classmethod
    def storeTmp(self):
        keys = [x for x in globals().keys()] # get variables now        
        dic = {}
        for key in keys:
            globals()['_addN'] = 0
            self.filter(globals()[key])
            if globals()['_addN'] != 0 : continue  # do not pickle unpicklable variables
            dic['_' + key] = globals()[key]   # add prefix to make sure it cannot confused with variables newly generated
        with open(globals()["__recodefile"],'wb') as f:
            pickle.dump(dic,f)

    @classmethod
    def logFuncTest(self,func):
        """
        this decorator can make recode point Test
        """
        def run(*args,**kargs):
            globals()["_nRunlst"].append(func.__name__) # recode func name
            # pass steps has already fininshed
            if globals().get("_aRunlst"):
                try:           
                    globals().get("_aRunlst").remove(func.__name__)
                    print("Pass")
                    return
                except:
                    raise Exception("running sequence change, please remove log file manually")

            # pass value to variables (last recode form log file); only run once
            if globals()["__runtag"] == 0:       
                for key in globals()["__dic"]:
                    if key == "___dic":continue
                    globals()[key[1:]] = globals()["__dic"][key]
                globals()["__runtag"] = 1

            now = time.time()
            print("Now Running: " + func.__name__)
            func(*args,**kargs)
            print("function over,use time: " + str((time.time() - now)))
            self.storeTmp() # recode every success run
        return run

    @classmethod
    def logFunc(self,func):
        """
        this decorator can make recode point 
        """
        def run(*args,**kargs):
            globals()["_nRunlst"].append(func.__name__) 
            if globals().get("_aRunlst"):
                try:           
                    globals().get("_aRunlst").remove(func.__name__)
                    return
                except:
                    raise Exception("running sequence change, please remove log file manually")

            if globals()["__runtag"] == 0:       
                for key in globals()["__dic"]:
                    if key == "___dic":continue
                    globals()[key[1:]] = globals()["__dic"][key]
                globals()["__runtag"] = 1

            func(*args,**kargs)
            self.storeTmp() 
        return run

    # if it end successfuly remove log file
    @classmethod
    def end(self):
        os.remove(globals()["__recodefile"])